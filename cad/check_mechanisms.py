from pathlib import Path
import json,math
import FreeCAD as App
import Part,MeshPart
ROOT=Path(__file__).resolve().parents[1]
def world(o):
    s=o.Shape.copy();s.Placement=o.getGlobalPlacement().multiply(o.Placement.inverse()).multiply(s.Placement);return s

def overlaps(a,b):
    x=a.BoundBox;y=b.BoundBox
    if any(getattr(x,k+'Max')<=getattr(y,k+'Min')+1e-6 or getattr(y,k+'Max')<=getattr(x,k+'Min')+1e-6 for k in 'XYZ'):return 0
    return a.common(b).Volume

def check(doc,parts):
    dim=doc.getObject('Dimensions');main=[r for r in parts if r['variant']=='main'];moving=[r for r in main if r['group']!='Base'];fixed=[r for r in main if r['group']=='Base']
    printed=[r for r in main if r['printed']]
    report={'status':'prototype; physical fit, friction and load tests pending','solids':len(parts),'default_geometry':all(r['valid'] and r['solids']==1 for r in parts)}
    # All intended components are included; cutters and intermediate features are not parts.
    dim.Tilt=0;doc.recompute();shapes={r['name']:world(doc.getObject(r['name'])) for r in main}
    hits=[]
    for i,a in enumerate(main):
        for b in main[i+1:]:
            v=overlaps(shapes[a['name']],shapes[b['name']])
            if v>.02:hits.append({'a':a['name'],'b':b['name'],'volume_mm3':round(v,3)})
    report['assembly_intersections']=hits
    print('assembly intersections',hits,flush=True)
    (ROOT/'work/mechanisms-20261014/contacts.json').write_text(json.dumps(hits,indent=2))
    if hits:
        (ROOT/'cad/mechanism-checks.json').write_text(json.dumps(report,indent=2)+'\n')
        raise AssertionError('Assembly intersections remain')
    rotation=[];fs={r['name']:shapes[r['name']] for r in fixed}
    for ang in range(0,360,15):
        contacts=[]
        for m in moving:
            s=shapes[m['name']].copy();s.rotate(App.Vector(0,0,dim.AxisHeight.Value),App.Vector(1,0,0),ang)
            for f in fixed:
                v=overlaps(s,fs[f['name']])
                if v>.02:contacts.append([m['name'],f['name'],round(v,3)])
        rotation.append({'angle':ang,'intersections':contacts})
    report['rotation_samples']=rotation
    dim.Tilt=20;doc.recompute()
    variants=[]
    for width in (30,116,160):
        dim.BoardWidth=width;doc.recompute()
        shapes={r['name']:world(doc.getObject(r['name'])) for r in main if r['printed'] or r['name']=='BoardEnvelope'}
        collisions=[];names=list(shapes)
        for i,a in enumerate(names):
            for b in names[i+1:]:
                v=overlaps(shapes[a],shapes[b])
                if v>.02:collisions.append([a,b,round(v,3)])
        variants.append({'width_mm':width,'board_width_mm':round(doc.getObject('BoardEnvelope').Shape.BoundBox.XLength,3),'intersections':collisions})
    report['board_widths']=variants
    dim.BoardWidth=116;dim.Tilt=20;doc.recompute()
    doc.save()
    # Export finished component shapes in assembly coordinates.
    ex=App.newDocument('MechanismExport');objects=[]
    for r in main:
        o=ex.addObject('Part::Feature',r['name']);o.Shape=world(doc.getObject(r['name']));objects.append(o)
    ex.recompute();Part.export(objects,str(ROOT/'exports/pcb-vise.step'))
    roundtrip=Part.Shape();roundtrip.read(str(ROOT/'exports/pcb-vise.step'))
    report['step']={'valid':roundtrip.isValid(),'solids':len(roundtrip.Solids),'expected':len(main)}
    App.closeDocument(ex.Name)
    exports=[]
    for r in parts:
        if not r['printed']:continue
        o=doc.getObject(r['name']);s=o.Shape.copy()
        # Orient bores and open nut pockets upward where practical.
        name=r['name'];orientation='as modelled, underside down'
        if 'JawBody' in name:
            angle=90 if name.startswith('Fixed') else -90
            s.rotate(App.Vector(),App.Vector(0,1,0),angle);orientation='adapter face down; rod bores vertical'
        elif 'Carrier' in name:
            angle=90 if name.startswith('Left') else -90
            s.rotate(App.Vector(),App.Vector(0,1,0),angle);orientation='inner flat face down; rod bores vertical'
        elif 'PivotKnob' in name:
            angle=90 if name.startswith('Left') else -90
            s.rotate(App.Vector(),App.Vector(0,1,0),angle);orientation='washer face down; nut entry up'
        elif 'EdgeGrip' in name:
            angle=-90 if name.startswith('Fixed') else 90
            s.rotate(App.Vector(),App.Vector(0,1,0),angle);orientation='jaw mounting face down'
        elif 'FrictionRing' in name:
            s.rotate(App.Vector(),App.Vector(0,1,0),90);orientation='flat ring face down'
        elif 'Shoe' in name:
            angle=90 if 'Front' in name else -90
            s.rotate(App.Vector(),App.Vector(1,0,0),angle);orientation='closed toe end down'
        bb=s.BoundBox;s.translate(App.Vector(-bb.XMin,-bb.YMin,-bb.ZMin))
        bb=s.BoundBox
        mesh=MeshPart.meshFromShape(Shape=s,LinearDeflection=.05,AngularDeflection=.15,Relative=False)
        path=ROOT/'exports/parts'/(r['name']+'.stl');mesh.write(str(path))
        exports.append({'part':r['name'],'orientation':orientation,'material':r['material'],'variant':r['variant'],'bounds_mm':[round(bb.XLength,2),round(bb.YLength,2),round(bb.ZLength,2)],'closed_mesh':mesh.isSolid(),'fits_p1s':max(bb.XLength,bb.YLength,bb.ZLength)<=256})
    report['stl_exports']=exports
    report['limits']=['Threads are simplified as clearance cylinders.','Rotation uses 15 degree samples and an unpopulated PCB envelope.','Split clamps and TPU feet require print and load tests.','Ballast mass and grip friction are not established.']
    (ROOT/'cad/mechanism-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'intersections':len(hits),'rotation_contacts':sum(len(x['intersections']) for x in rotation),'step':report['step'],'printed_parts':len(exports),'stl_pass':all(e['closed_mesh'] and e['fits_p1s'] for e in exports)}),flush=True)
    assert report['step']['valid'] and report['step']['solids']==report['step']['expected']
    assert not any(r['intersections'] for r in rotation+variants)
    assert all(e['closed_mesh'] and e['fits_p1s'] for e in exports)
    return report

if __name__=='__main__':
    doc=App.openDocument(str(ROOT/'cad/pcb-vise.FCStd'))
    check(doc,json.loads((ROOT/'cad/parts.json').read_text()))

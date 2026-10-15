"""Build the vise prototype with native FreeCAD primitives and boolean features."""
from pathlib import Path
import json, math
import FreeCAD as App
import Part, MeshPart
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'exports'
DOC='PCB_Vise_Mechanisms'
COLORS={'frame':(0.16,0.25,0.30),'jaw':(0.12,0.55,0.57),'soft':(0.94,0.58,0.19),'steel':(0.70,0.73,0.76),'board':(0.15,0.40,0.24)}

def build(esc=False):
    docname=DOC+('_ESC' if esc else '')
    stem='pcb-vise-esc' if esc else 'pcb-vise'
    if docname in App.listDocuments(): App.closeDocument(docname)
    d=App.newDocument(docname)
    dims=d.addObject('App::FeaturePython','Dimensions')
    for k,v in {'BoardWidth':116 if esc else 100,'BoardDepth':112 if esc else 80,'BoardThickness':1.6,'AxisHeight':125,'GuideBore':8.3,'AdapterLift':10,'GripHeight':10}.items():
        dims.addProperty('App::PropertyLength',k,'Dimensions');setattr(dims,k,v)
    dims.addProperty('App::PropertyString','Configuration','Notes');dims.Configuration='ESC adapters' if esc else 'edge grips'
    dims.addProperty('App::PropertyAngle','Tilt','Dimensions');dims.Tilt=20
    dims.addProperty('App::PropertyString','Status','Notes');dims.Status='Prototype for fit testing. Not load-tested.'
    base=d.addObject('App::Part','Base')
    rotor=d.addObject('App::Part','RotatingFrame');rotor.Placement=App.Placement(App.Vector(0,0,125),App.Rotation(App.Vector(1,0,0),20))
    rotor.setExpression('Placement.Base.z','Dimensions.AxisHeight');rotor.setExpression('Placement.Rotation.Angle','Dimensions.Tilt')
    fixed=d.addObject('App::Part','FixedJaw');rotor.addObject(fixed)
    sliding=d.addObject('App::Part','SlidingJaw');rotor.addObject(sliding);sliding.setExpression('Placement.Base.x','Dimensions.BoardWidth - 116 mm' if esc else 'Dimensions.BoardWidth - 116 mm + Dimensions.BoardThickness')
    alternatives=d.addObject('App::Part','AlternativeGrips');alternatives.Placement=rotor.Placement
    manifest=[];hw=[]
    def setval(o,k,v):
        if isinstance(v,str):o.setExpression(k,v)
        else:setattr(o,k,v)
    def pos(o,xyz):
        pl=o.Placement
        for axis,v in zip('xyz',xyz):
            if not isinstance(v,str):setattr(pl.Base,axis,v)
        o.Placement=pl
        for axis,v in zip('xyz',xyz):
            if isinstance(v,str):o.setExpression('Placement.Base.'+axis,v)
    def box(n,xyz,size):
        o=d.addObject('Part::Box',n)
        for k,v in zip(('Length','Width','Height'),size):setval(o,k,v)
        pos(o,xyz);return o
    def cyl(n,xyz,r,h,axis='z'):
        o=d.addObject('Part::Cylinder',n);setval(o,'Radius',r);setval(o,'Height',h)
        o.Placement.Rotation=App.Rotation(App.Vector(0,0,1),App.Vector({'x':(1,0,0),'y':(0,1,0),'z':(0,0,1)}[axis]))
        pos(o,xyz);return o
    def hexagon(n,xyz,af,h,axis='z'):
        o=d.addObject('Part::Prism',n);o.Polygon=6;o.Circumradius=af/math.sqrt(3);o.Height=h
        o.Placement.Rotation=App.Rotation(App.Vector(0,0,1),App.Vector({'x':(1,0,0),'y':(0,1,0),'z':(0,0,1)}[axis]))
        pos(o,xyz);return o
    def fuse(n,objs):
        o=d.addObject('Part::MultiFuse',n);o.Shapes=objs;return o
    def cut(n,obj,tools):
        t=tools[0] if len(tools)==1 else fuse(n+'Cutters',tools)
        o=d.addObject('Part::Cut',n);o.Base=obj;o.Tool=t;return o
    def finish(o,g,material='PETG-CF',color='frame',variant='main'):
        if not esc and any(t in o.Name for t in ('MountingAdapter','BoardScrew','BoardNut','BoardWasher')):variant='esc'
        if 'EdgeGrip' in o.Name:variant='alternative' if esc else 'main'
        g.addObject(o)
        o.addProperty('App::PropertyString','Material','Part');o.Material=material
        if App.GuiUp:o.ViewObject.ShapeColor=COLORS[color];o.ViewObject.LineColor=(.08,.1,.12)
        manifest.append({'name':o.Name,'group':g.Name,'material':material,'variant':variant,'color':COLORS[color],'printed':material in ('PETG-CF','TPU for AMS')})
        return o
    def screw(n,g,xyz,m,length,axis='z',head='cap'):
        # xyz is the thread tip, with the head at the positive end of the chosen axis.
        dh={3:5.68,4:7.22,5:8.72,6:10}[m];hh={3:3,4:4,5:5,6:4}[m]
        end=list(xyz);axis_i='xyz'.index(axis)
        end[axis_i]=(end[axis_i]+f' + {length:g} mm') if isinstance(end[axis_i],str) else end[axis_i]+length
        sh=cyl(n+'Shaft',xyz,m/2,length,axis)
        hd=hexagon(n+'Head',end,10,4,axis) if head=='hex' else cyl(n+'Head',end,dh/2,hh,axis)
        o=finish(fuse(n,[sh,hd]),g,'steel','steel')
        hw.append({'part':f'M{m} x {length:g} '+('hex bolt DIN 933' if head=='hex' else 'socket cap screw DIN 912'),'quantity':1,'reference':o.Name})
        return o
    def nut(n,g,xyz,m,axis='z'):
        af,h={3:(5.5,2.4),4:(7,3.2),5:(8,4),6:(10,5)}[m]
        o=cut(n,hexagon(n+'Blank',xyz,af,h,axis),[cyl(n+'Hole',xyz,m/2+.05,h,axis)])
        finish(o,g,'steel','steel');hw.append({'part':f'M{m} nut DIN 934, {af:g} mm AF x {h:g} mm','quantity':1,'reference':o.Name})
    def washer(n,g,xyz,m,od,h,axis='z'):
        o=cut(n,cyl(n+'Blank',xyz,od/2,h,axis),[cyl(n+'Hole',xyz,{3:3.2,4:4.3,5:5.3,6:6.4}[m]/2,h,axis)])
        finish(o,g,'steel','steel');hw.append({'part':f'M{m} washer, {od:g} mm OD x {h:g} mm','quantity':1,'reference':o.Name})

    # Foot pockets, removable ballast covers and matching upright fasteners.
    for side,x in [('Left',-147),('Right',147)]:
        blank=box(side+'FootBlank',(x-29,-120,4),(58,240,26));tools=[]
        for i,y in enumerate((-108,43)):tools.append(box(side+'BallastPocket'+str(i),(x-23,y,10),(46,65,22)))
        for y in (-18,18):
            slotx=x-.2 if x<0 else x-29.2
            tools.append(box(side+'BarSeat',(slotx,y-8.2,7.8),(29.4,16.4,8.4)))
        for i,(dx,y) in enumerate([(-16,-18),(16,-18),(-16,18),(16,18)]):
            px=x+dx;tools += [cyl(side+'BaseThrough'+str(i),(px,y,3),2.75,38),hexagon(side+'BaseNutPocket'+str(i),(px,y,5.8),8.3,4.4),cyl(side+'BaseNutEntry'+str(i),(px,y,3),4.95,2.8)]
            screw(side+'BaseScrew'+str(i),base,(px,y,4),5,35)
            washer(side+'BaseWasher'+str(i),base,(px,y,38),5,10,1)
            nut(side+'BaseNut'+str(i),base,(px,y,6),5)
        for y in (-114,-37,37,114):
            tools += [cyl(side+'LidBore',(x,y,3),1.7,34),hexagon(side+'LidNutPocket',(x,y,5.8),5.8,2.8),cyl(side+'LidNutEntry',(x,y,3),3.5,2.8)]
            screw(side+'LidScrew'+str(y),base,(x,y,3),3,30)
            nut(side+'LidNut'+str(y),base,(x,y,6),3)
        finish(cut(side+'Foot',blank,tools),base)
        for label,ys,holes in [('Front',-117,(-114,-37)),('Rear',34,(37,114))]:
            lid=box(side+label+'LidBlank',(x-25,ys,30),(50,83,3))
            finish(cut(side+label+'BallastLid',lid,[cyl(side+label+'LidHole',(x,y,29),1.7,5) for y in holes]),base)
        flange=box(side+'Flange',(x-25,-27,30),(50,54,8))
        web=box(side+'Web',(x-7,-23,38),(14,46,'Dimensions.AxisHeight - 38 mm'))
        crown=cyl(side+'Crown',(x-7,0,'Dimensions.AxisHeight'),23,14,'x')
        tools=[cyl(side+'PivotBore',(x-8,0,'Dimensions.AxisHeight'),3.3,16,'x')]
        tools += [cyl(side+'FlangeHole',(x+dx,y,29),2.75,10) for dx,y in [(-16,-18),(16,-18),(-16,18),(16,18)]]
        finish(cut(side+'Upright',fuse(side+'UprightBlank',[flange,web,crown]),tools),base)
        # Slip-on TPU shoes: no adhesives or screws under the ballast pockets.
        for end in (-1,1):
            y0=100 if end>0 else -122.5
            floor=box(side+'ShoeFloor',(x-31.5,y0,0),(63,22.5,4))
            outery=120.3 if end>0 else -122.5
            parts=[floor,box(side+'ShoeEnd',(x-31.5,outery,4),(63,2.2,28.3))]
            for dx in (-31.5,29.3):parts.append(box(side+'ShoeWall',(x+dx,y0,4),(2.2,22.5,28.3)))
            for dx in (-31.5,26.5):parts.append(box(side+'ShoeLip',(x+dx,y0,30.3),(5,22.5,2)))
            shoe=fuse(side+'ShoeBlank',parts)
            relief=cyl(side+'ShoeBoltRelief',(x,114*end,2.5),2,2)
            finish(cut(side+('FrontShoe' if end<0 else 'RearShoe'),shoe,[relief]),base,'TPU for AMS','soft')

    # Two bolted lap joints, with their nuts accessible before the base is fitted.
    for rail,y in [('Front',-18),('Rear',18)]:
        for side,x in [('Left',-147),('Right',-20)]:
            b=box(side+rail+'TieBlank',(x,y-8,8),(167,16,8))
            lapz=11.9 if side=='Left' else 7.9
            laph=4.2 if side=='Left' else 4.2
            tools=[box(side+rail+'Lap',(-20.1,y-8.1,lapz),(40.2,16.2,laph))]
            tools += [cyl(side+rail+'JointBore',(px,y,7),2.25,10) for px in (-10,10)]
            px=-131 if side=='Left' else 131
            tools += [cyl(side+rail+'FootBore',(px,y,7),2.75,10),hexagon(side+rail+'NutClearance',(px,y,5.8),8.3,4.4)]
            finish(cut(side+rail+'Tie',b,tools),base)
        for i,px in enumerate((-10,10)):
            screw(rail+'JointScrew'+str(i),base,(px,y,4),4,12)
            nut(rail+'JointNut'+str(i),base,(px,y,4.8),4)

    for side,sign in [('Left',-1),('Right',1)]:
        capx=-130 if sign<0 else 114
        cap=box(side+'CarrierBlank',(capx,-39,-47),(16,78,70))
        tools=[cyl(side+'GuideSeat',( -125.5 if sign<0 else 114,y,-35),4.15,11.5,'x') for y in (-28,28)]
        tools += [cyl(side+'CarrierPivotBore',(capx-1,0,0),3.3,18,'x')]
        disk=cyl(side+'FrictionFace',(-138 if sign<0 else 130,0,0),23,8,'x')
        cap=fuse(side+'CarrierAndDisc',[cut(side+'CarrierBored',cap,tools),disk])
        tools=[cyl(side+'DiscBore',(-139 if sign<0 else 129,0,0),3.3,10,'x')]
        tools += [hexagon(side+'BoltHeadPocket',(-120 if sign<0 else 113,0,0),10.3,7,'x')]
        finish(cut(side+'Carrier',cap,tools),rotor,'PETG-CF','jaw')
        face=cut(side+'FrictionRing',cyl(side+'FrictionRingBlank',(-140 if sign<0 else 138,0,0),22,2,'x'),[cyl(side+'RingHole',(-140 if sign<0 else 138,0,0),3.3,2,'x')])
        finish(face,rotor,'TPU for AMS','soft')
        # Mirrored bolt placements; thread length is measured from under the head.
        if sign<0:screw(side+'PivotBolt',rotor,(-169.5,0,0),6,50,'x','hex')
        else:
            bolt=screw(side+'PivotBolt',rotor,(-169.5,0,0),6,50,'x','hex')
            bolt.Placement=App.Placement(App.Vector(),App.Rotation(App.Vector(0,0,1),180))
        washer(side+'PivotWasher',base,(-155.6 if sign<0 else 154,0,'Dimensions.AxisHeight'),6,12,1.6,'x')
        kx=-173 if sign<0 else 155.6
        knobparts=[cyl(side+'KnobCore',(kx,0,'Dimensions.AxisHeight'),17,17.4,'x')]
        for y,z in [(16,'Dimensions.AxisHeight'),(-16,'Dimensions.AxisHeight'),(0,'Dimensions.AxisHeight + 16 mm'),(0,'Dimensions.AxisHeight - 16 mm')]:knobparts.append(cyl(side+'KnobLobe',(kx,y,z),7,17.4,'x'))
        cuts=[cyl(side+'KnobBore',(kx-1,0,'Dimensions.AxisHeight'),3.3,20,'x'),hexagon(side+'KnobNutPocket',(-167.2 if sign<0 else 162,0,'Dimensions.AxisHeight'),10.3,5.2,'x'),cyl(side+'KnobNutEntry',(-174 if sign<0 else 167.2,0,'Dimensions.AxisHeight'),6.1,6.8,'x')]
        finish(cut(side+'PivotKnob',fuse(side+'KnobBlank',knobparts),cuts),base,'PETG-CF','soft')
        nut(side+'PivotNut',base,(-167 if sign<0 else 162,0,'Dimensions.AxisHeight'),6,'x')
    for i,y in enumerate((-28,28)):
        finish(cyl('GuideRod'+str(i),(-125,y,-35),4,250,'x'),rotor,'steel','steel');hw.append({'part':'8 x 250 mm smooth steel rod','quantity':1,'reference':'GuideRod'+str(i)})

    for side,g,bx,sign in [('Fixed',fixed,-112,-1),('Sliding',sliding,26,1)]:
        b=box(side+'JawBlank',(bx,-45,-45),(18,90,46))
        cuts=[cyl(side+'RodBore',(bx-1,y,-35),'Dimensions.GuideBore / 2',20,'x') for y in (-28,28)]
        cuts += [box(side+'ClampSlit',(bx-1,-46,-35.4),(20,18,0.8)),cyl(side+'ClampBore',(bx+9,-38,-46),2.25,48),hexagon(side+'ClampNutPocket',(bx+9,-38,-45.1),7.3,3.6)]
        for y in (-20,20):
            cuts.append(cyl(side+'AdapterBore',(bx-1,y,-7),1.7,20,'x'))
            hx=-104 if sign<0 else 33
            cuts += [hexagon(side+'AdapterNutPocket',(hx,y,-7),5.8,3,'x'),cyl(side+'AdapterNutEntry',(-113 if sign<0 else 36,y,-7),3.5,9,'x')]
        finish(cut(side+'JawBody',b,cuts),g,'PETG-CF','jaw')
        screw(side+'ClampScrew',g,(bx+9,-38,-48.2),4,50)
        washer(side+'ClampWasher',g,(bx+9,-38,1),4,9,.8)
        nut(side+'ClampNut',g,(bx+9,-38,-44.8),4)
        ax=-94 if sign<0 else 13;holex=-88.5 if sign<0 else 20.5
        rail=box(side+'AdapterRail',(ax,'-Dimensions.BoardDepth / 2 - 4 mm',-13),(13,'Dimensions.BoardDepth + 8 mm',8))
        bosses=[cyl(side+'Standoff',(holex,y,-5),3.2,'Dimensions.AdapterLift + 4.2 mm') for y in ('-Dimensions.BoardDepth / 2 + 3.5 mm','Dimensions.BoardDepth / 2 - 3.5 mm')]
        cuts=[]
        for y in ('-Dimensions.BoardDepth / 2 + 3.5 mm','Dimensions.BoardDepth / 2 - 3.5 mm'):
            cuts += [cyl(side+'BoardBore',(holex,y,-14),1.7,'Dimensions.AdapterLift + 16 mm'),hexagon(side+'BoardNutPocket',(holex,y,-13.1),5.8,3)]
        for y in (-20,20):cuts.append(cyl(side+'AdapterScrewHole',(ax-1,y,-7),1.7,15,'x'))
        finish(cut(side+'MountingAdapter',fuse(side+'AdapterBlank',[rail]+bosses),cuts),g,'PETG-CF','soft')
        for i,y in enumerate(('-Dimensions.BoardDepth / 2 + 3.5 mm','Dimensions.BoardDepth / 2 - 3.5 mm')):
            screw(side+'BoardScrew'+str(i),g,(holex,y,'Dimensions.AdapterLift - 23.7 mm'),3,25)
            washer(side+'BoardWasher'+str(i),g,(holex,y,'Dimensions.AdapterLift + 0.8 mm'),3,7,.5)
            nut(side+'BoardNut'+str(i),g,(holex,y,-12.7),3)
        for i,y in enumerate((-20,20)):
            if sign<0:screw(side+'AdapterScrew'+str(i),g,(-106 if esc else -108,y,-7),3,25 if esc else 20,'x')
            else:
                # A negative-axis screw is expressed as a rotated native bolt.
                bolt=screw(side+'AdapterScrew'+str(i),g,(-38 if esc else -40,-y,-7),3,25 if esc else 20,'x')
                bolt.Placement=App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),180))
            nut(side+'AdapterNut'+str(i),g,(-103.8 if sign<0 else 33.4,y,-7),3,'x')
        # The same V grooves seat thin and thick boards when the jaws are moved in.
        gripx=-94 if sign<0 else 20
        rail=box(side+'EdgeRail',(gripx,-31,-13),(6,62,8))
        lipx=-94 if sign<0 else 21
        lip=box(side+'EdgeLip',(lipx,-31,-5),(5,62,'Dimensions.GripHeight + 10 mm'))
        tipx=-92 if sign<0 else 24
        groove=box(side+'EdgeGroove',(tipx,-32,'Dimensions.GripHeight'),(6,64,6))
        groove.Placement.Rotation=App.Rotation(App.Vector(0,1,0),45 if sign<0 else 225)
        cuts=[groove]+[cyl(side+'EdgeMountHole',(gripx-1,y,-7),1.7,8,'x') for y in (-20,20)]
        finish(cut(side+'EdgeGrip',fuse(side+'EdgeBlank',[rail,lip]),cuts),g,'TPU for AMS','soft','alternative')
    boardx=-92 if esc else '-92 mm + Dimensions.BoardThickness / 2'
    height='Dimensions.AdapterLift' if esc else 'Dimensions.GripHeight'
    plate=box('BoardEnvelopeBlank' if esc else 'BoardEnvelope',(boardx,'-Dimensions.BoardDepth / 2',height+' - Dimensions.BoardThickness / 2'),('Dimensions.BoardWidth','Dimensions.BoardDepth','Dimensions.BoardThickness'))
    if esc:
        holes=[cyl('BoardHole',(x,y,'Dimensions.AdapterLift - 2 mm'),1.6,4) for x in (-88.5,'Dimensions.BoardWidth - 95.5 mm') for y in ('-Dimensions.BoardDepth / 2 + 3.5 mm','Dimensions.BoardDepth / 2 - 3.5 mm')]
        plate=cut('BoardEnvelope',plate,holes)
    finish(plate,rotor,'reference PCB','board')
    for side,x in [('Left',-147),('Right',147)]:
        for label,y in [('Front',-75.5),('Rear',75.5)]:
            tray=box(side+label+'LinerBlank',(x-22,y-31.5,10),(44,63,19.45))
            cavity=box(side+label+'LinerCavity',(x-19.5,y-30.5,10.4),(39,61,20))
            finish(cut(side+label+'BallastLiner',tray,[cavity]),base,'TPU for AMS','soft')
            block=box(side+label+'Ballast',(x-19.05,y-30,10.4),(38.1,60,19.05))
            finish(block,base,'steel','steel')
            hw.append({'part':'Steel ballast, 38.1 x 60 x 19.05 mm','quantity':1,'reference':block.Name})
    d.recompute()
    names={r['name'] for r in manifest if r['variant']=='main'}
    if App.GuiUp:
        for o in d.Objects:
            if o.TypeId!='App::Part':o.ViewObject.Visibility=o.Name in names
        alternatives.ViewObject.Visibility=False
        for g in (base,rotor,fixed,sliding):g.ViewObject.Visibility=True
        Gui.activeDocument().activeView().viewAxonometric();Gui.activeDocument().activeView().fitAll()
    for r in manifest:
        o=d.getObject(r['name']);r['valid']=o.Shape.isValid();r['solids']=len(o.Shape.Solids);r['volume_mm3']=round(o.Shape.Volume,3)
        if not r['valid'] or r['solids']!=1:raise ValueError(r)
    d.saveAs(str(ROOT/'cad'/(stem+'.FCStd')))
    (ROOT/'cad'/('parts-esc.json' if esc else 'parts.json')).write_text(json.dumps(manifest,indent=2)+'\n')
    (ROOT/'work/mechanisms-20261014/hardware.json').write_text(json.dumps(hw,indent=2)+'\n')
    if App.GuiUp and not esc:Gui.activeDocument().activeView().saveImage(str(OUT/'mechanisms-preview.png'),1800,1300,'White')
    return d,manifest,hw

if __name__=='__main__':
    build()

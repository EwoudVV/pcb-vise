"""Check the edge grips against board and component envelopes."""
from pathlib import Path
import itertools
import json
import math
import FreeCAD as App
import Part
from check_mechanisms import world, overlaps

ROOT = Path(__file__).resolve().parents[1]

def check():
    doc = App.openDocument(str(ROOT / 'cad/pcb-vise.FCStd'))
    dim = doc.Dimensions
    initial = {k: getattr(dim, k).Value for k in ('BoardWidth', 'BoardDepth', 'BoardThickness', 'Tilt')}
    dim.Tilt = 0
    rows = [r for r in json.loads((ROOT / 'cad/parts.json').read_text()) if r['variant'] == 'main']
    cases = []
    for width, depth, thickness in itertools.product((30, 60, 100, 160), (30, 80, 160), (.8, 1.6, 2.4)):
        dim.BoardWidth = width
        dim.BoardDepth = depth
        dim.BoardThickness = thickness
        doc.recompute()
        shapes = {r['name']: world(doc.getObject(r['name'])) for r in rows}
        board = shapes['BoardEnvelope']
        bb = board.BoundBox
        edge = 3
        top = Part.makeBox(width-2*edge, depth-2*edge, 25, App.Vector(bb.XMin+edge, bb.YMin+edge, bb.ZMax))
        bottom = Part.makeBox(width-2*edge, depth-2*edge, 10, App.Vector(bb.XMin+edge, bb.YMin+edge, bb.ZMin-10))
        contacts = []
        for label, shape in [('board', board), ('top components', top), ('bottom components', bottom)]:
            for name, other in shapes.items():
                if name == 'BoardEnvelope':
                    continue
                volume = overlaps(shape, other)
                if volume > .001:
                    contacts.append([label, name, round(volume, 4)])
        seating = [round(board.distToShape(shapes[n])[0], 6) for n in ('FixedEdgeGrip', 'SlidingEdgeGrip')]
        # A short straight probe represents tip access, not the whole soldering iron.
        tool_contacts = []
        for x, y in itertools.product((bb.XMin+9, (bb.XMin+bb.XMax)/2, bb.XMax-9), (-depth/2+3, 0, depth/2-3)):
            probe = Part.makeCylinder(2, 35, App.Vector(x, y, bb.ZMin-35))
            for name, other in shapes.items():
                if name != 'BoardEnvelope' and overlaps(probe, other) > .001:
                    tool_contacts.append(name)
        # Bounding boxes enclose the complete circular sweep around the pivot axis.
        axis = dim.AxisHeight.Value
        sweep_gaps = []
        for envelope in (board, top, bottom):
            bounds = envelope.BoundBox
            radius = max(math.hypot(y, z-axis) for y in (bounds.YMin, bounds.YMax) for z in (bounds.ZMin, bounds.ZMax))
            for r in rows:
                if r['group'] != 'Base':
                    continue
                fixed = shapes[r['name']].BoundBox
                if bounds.XMax <= fixed.XMin or bounds.XMin >= fixed.XMax:
                    continue
                ymin = 0 if fixed.YMin <= 0 <= fixed.YMax else min(abs(fixed.YMin), abs(fixed.YMax))
                zmin = 0 if fixed.ZMin <= axis <= fixed.ZMax else min(abs(fixed.ZMin-axis), abs(fixed.ZMax-axis))
                sweep_gaps.append(math.hypot(ymin, zmin)-radius)
        case = {'width_mm': width, 'depth_mm': depth, 'thickness_mm': thickness,
                'contacts': contacts, 'grip_contact_distances_mm': seating,
                'tip_access_contacts': sorted(set(tool_contacts)),
                'fixed_base_rotation_gap_lower_bound_mm': round(min(sweep_gaps), 3)}
        cases.append(case)
        print(width, depth, thickness, contacts, seating, sorted(set(tool_contacts)), flush=True)
    for key, value in initial.items():
        setattr(dim, key, value)
    doc.recompute()
    report = {'component_edge_clearance_mm': 3, 'top_component_height_mm': 25,
              'bottom_component_height_mm': 10, 'straight_tip_probe_diameter_mm': 4,
              'straight_tip_probe_length_mm': 35, 'tip_access_inset_from_gripped_edges_mm': 9,
              'cases': cases, 'limits': ['Rectangular board envelopes, not every possible component or connector.',
              'V-groove contact is nominal geometry; printed grip and holding force need testing.',
              'The probe does not represent an iron handle or angled access.']}
    (ROOT / 'cad/general-grip-checks.json').write_text(json.dumps(report, indent=2)+'\n')
    assert all(not c['contacts'] and not c['tip_access_contacts'] and max(c['grip_contact_distances_mm']) < .00001 and c['fixed_base_rotation_gap_lower_bound_mm'] > 0 for c in cases)
    return report

if __name__ == '__main__':
    check()

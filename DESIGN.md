# rotating pcb vise

a freestanding holder for soldering and inspecting boards. the first board to fit is the 116 x 112 mm ESC, but the jaws should adjust for smaller projects too

## starting targets

these are design targets, not measured performance

- 30-160 mm distance between the board grips
- support a board up to 160 mm across the rotation direction
- full rotation, with a lock that holds the board while soldering
- replaceable edge grips, with clearance for parts on both sides
- a stable base with rubber feet and space for removable ballast
- metal guide rods and ordinary metric fasteners
- split printed parts to keep the required print area manageable
- used for hand soldering and inspection; take the board out for reflow

## first mechanism to check

two uprights support a rotating frame. one jaw stays fixed in the frame and the other slides on two metal rods. a small screw provides the final clamping adjustment after sliding the jaw into position. keep that clamping force low enough to avoid bending the PCB

one pivot gets a locking knob. the frame needs to carry the lock's torque to the other side without twisting. compare a friction disc against an indexed face before choosing the final lock

use replaceable jaw inserts so different PCB thicknesses and crowded edges can be handled without reprinting the frame. start with a 1.6 mm board sample. the ESC mounting holes offer another support option if its edge components obstruct the grips

## checks before detailed CAD

1. pick actual rods, screws, nuts, washers and feet with dimensions and prices
2. check the ESC outline and component envelope where the jaws would touch
3. work out the full rotation clearance, including components and the frame
4. check the base against tipping and sliding when pressing on the board
5. make small fit samples for rod holes, nut pockets, jaw grooves and the pivot lock
6. verify clamp travel and assembly access before adding cosmetic details

## files to make

- editable FreeCAD assembly and part features
- STEP assembly and individual printable models
- dimensioned assembly views and hardware BOM
- fit samples and printing notes
- renders and assembly instructions

## week plan

- Monday: scope, mechanism, hardware dimensions and quotes
- Tuesday-Wednesday: first assembly and interference checks
- Thursday-Friday: fit samples if printer access is available, then revisions
- Saturday: exports, BOM, instructions and renders
- Sunday: final review and submission

## still to confirm

printer: Bambu P1S, with PLA, Bambu TPU for AMS and PETG-CF available. use a 256 x 256 mm print area. nozzle type, hardware already owned, ballast and the final budget still need confirming. FreeCAD 1.1.4 is installed and the first layout is saved. all 27 parts are valid solids; the STEP round-trip contains 27 solids. 24 sampled rotations show no intersections between the rotating assembly and the base. the board and jaw parameters recompute at 30, 116 and 160 mm. these checks use the unpopulated board envelope and do not verify strength, fastener retention or the populated ESC. no physical test has been completed yet

## edge-clearance check

the first pad check found conflicts in the ESC's right-side 2 mm edge strip across the proposed central grip region. the left-side strip had no pad hits in that region, but that does not prove clearance from component bodies. the first assembly therefore uses the four mounting holes. generic removable edge grips remain part of the plan

## October 14 mechanism checkpoint

current model: cad/pcb-vise.FCStd. the split jaw clamps, interchangeable inserts, captured pivot hardware, base lap joints, ballast lids and TPU shoes are now modelled. use ASSEMBLY.md and HARDWARE.md for the current assembly and fastener details. the older layout remains as a checkpoint

109 main assembly solids and two alternative edge grips pass the solid checks. the default assembly has no detected overlaps, 24 rotation samples are clear, and both insert configurations were checked at 30, 116 and 160 mm board widths. all 28 part STL meshes are closed and fit the P1S envelope. physical fit, holding force, ballast and populated-board clearance remain untested

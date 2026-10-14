# rotating pcb vise

[Half Life project](https://halflife.hackclub.com/projects/cmv5uxwy90kuh01n00i6f4u88)

a freestanding holder for soldering and inspecting PCBs. the jaws slide on steel rods, and the frame turns over so both sides of the board are reachable

![vise assembly](exports/mechanisms-preview.png)

## current design

the prototype now has split jaw clamps, removable inserts, M6 pivot knobs, bolted base joints, ballast lids and slip-on TPU feet. the ESC adapters use its existing 109 x 105 mm mounting-hole pattern. a second pair of TPU inserts grips the edges of ordinary boards

nothing has been printed or load-tested yet. the green plate is an unpopulated board envelope, not a model of the ESC's components. start with the fit samples and one clamp before printing the full set

## how it fits together

- M4 screws close the split jaws around the front guide rod. slide the jaws into light contact with the board, then lock them with an Allen key
- each insert attaches with two M3 screws and captured nuts. swap the rigid mounting-hole adapters for TPU edge grips using the same fasteners
- M6 bolts have their heads captured in the carriers. printed knobs with captured M6 nuts squeeze TPU friction rings against the uprights
- the base bars join with bolted lap joints and sit in recesses under the uprights
- four screw-on lids retain the ballast. the TPU feet slide over the base ends and have relief around the lid-screw tips

![jaw clamp and adapter](exports/jaw-detail.png)

## files

- [cad/pcb-vise.FCStd](cad/pcb-vise.FCStd): current editable FreeCAD assembly
- [exports/pcb-vise.step](exports/pcb-vise.step): current assembly export
- [exports/parts/](exports/parts/): 28 oriented prototype STLs, including two alternative edge grips
- [ASSEMBLY.md](ASSEMBLY.md): assembly order, printing notes and physical checks
- [HARDWARE.md](HARDWARE.md) and [hardware.csv](hardware.csv): fastener sizes and quantities for one vise
- [fit samples](exports/fit-tests/README.md): rod and nut-pocket checks before the larger prints
- [cad/mechanism-checks.json](cad/mechanism-checks.json): geometry, rotation and mesh check results

`pcb-vise-layout.FCStd` and `pcb-vise-layout.step` are the earlier layout checkpoint. use `pcb-vise.FCStd` for the current design

## CAD and checks

the FreeCAD file keeps the native primitive and boolean features. the Dimensions object controls board size, guide-bore clearance, axis height and rotation angle. [cad/build_mechanisms.py](cad/build_mechanisms.py) builds the prototype and [cad/check_mechanisms.py](cad/check_mechanisms.py) checks and exports it using FreeCAD's Python modules

the main assembly has 109 valid solids, including the simplified hardware. the two alternative edge grips are separate. no assembly overlaps were detected, and the rotating frame clears the fixed parts at 24 sampled angles. both insert configurations were checked at board widths of 30, 116 and 160 mm. the STEP file imports with all 109 solids, and all 28 STL meshes are closed and fit the P1S envelope

these checks do not establish strength, continuous swept clearance, friction or fit around real components. fastener threads are simplified cylinders. the clamp, TPU pads, base stability and populated-board clearances still need physical tests

## printer and materials

the printer is a Bambu P1S. PLA, PETG-CF and TPU for AMS are available. use PLA for the first fit checks, PETG-CF as the structural-material candidate, and TPU for the rings, feet and edge grips. Bambu specifies a hardened-steel nozzle for PETG-CF; nozzle type is still to be confirmed

the largest parts fit within the 256 x 256 mm bed. inspect the nut-pocket ceilings, blind rod holes and horizontal fastener holes in the slicer before printing. the PCB comes out of the holder for reflow

## parts and next steps

the hardware list now has exact sizes and quantities, but it is not a finished shopping cart. purchasing sources, shipping, ballast and the total cost still need checking. the website BOM is managed separately through Half Life

next are the fit prints, one jaw-clamp test, the pivot holding test and a stability check with representative board mass. then adjust the clearances and finish the purchase BOM

## references

- [guide rod reference](https://abra-electronics.com/robotics/axles-rods/mp-rm8-250-8mm-m8-250mm-linear-shaft-rail-rod.html)
- [DIN 934 nut dimensions](https://www.westfieldfasteners.co.uk/Standards/Nut_Hex_M.html)
- [DIN 912 screw dimensions](https://www.boltking.co.uk/din-912)
- [Bambu PETG-CF printing guidance](https://us.store.bambulab.com/collections/bambu-lab-3d-printer-filament/products/petg-cf)

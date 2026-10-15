# pcb vise design plan

this week is for finishing the design. printing, assembly and physical tests belong to build week

## current design

- freestanding base with covered ballast pockets and removable TPU feet
- two 8 x 250 mm guide rods
- jaws that slide along the rods and lock with M4 screws
- M6 pivot bolts and knobs, with TPU friction rings
- removable mounting-hole adapters for the ESC
- a second pair of TPU edge grips for other boards
- base bars with bolted lap joints

the current model is `cad/pcb-vise.FCStd`. the files with `layout` in their names are the earlier version

## remaining design work

1. check the populated ESC against the adapters, jaws and frame. include screw heads, connectors, cable bends and access for soldering tools
2. review the rotation clearance throughout the movement, including the largest intended board and its components
3. work out the ballast volume, expected mass and tipping limits. choose the weight material and decide whether the base dimensions need changing
4. review the clamp slit, pivot friction surfaces and fastener joints. check wall thickness, screw engagement and access to each nut
5. choose actual suppliers and hardware. check tolerances and make a priced BOM with shipping
6. add dimensioned drawings for the fits and joints. keep untested print allowances clearly identified
7. review the print orientations, bridges, supports and material use in Bambu Studio. adjust the models before making the final exports
8. finish the README, assembly drawings, website BOM, cart screenshots and closing reel for submission

## targets to confirm

- boards 30-160 mm wide
- up to 160 mm across the direction of rotation
- replaceable grips for different board thicknesses
- full rotation with room for components and cables
- a stable base that stays put during soldering
- every printed part fits the P1S bed

the current model uses a 1.6 mm board. the ESC mounting pattern is 109 x 105 mm. its crowded right edge is why the first adapters use mounting holes

## materials and hardware

the available printer is a Bambu P1S. PLA, PETG-CF and TPU for AMS are available. the hardened-steel nozzle needed for PETG-CF still needs confirming

use HARDWARE.md and hardware.csv for the current sizes and quantities. those are not final supplier quotes yet

## build week

start with the small rod and nut-pocket samples, then one jaw clamp. use the results to adjust the fits before printing the full set. after assembly, check pivot holding force, foot retention, sliding and tipping with a representative board

none of those physical tests has happened yet. keep the results separate from the CAD checks already saved in the repo

## October 15 update

reviewed the holder with the available ESC component models and extra space reserved for the missing models and connectors. the XT60 needs to face the unused rod length. the ESC adapters now lift the board 10 mm and use M3 x 25 mounting screws

the feet are now 240 mm long with deeper ballast pockets. four 38.1 x 60 x 19.05 mm steel blocks sit in TPU liners under the lids. the upright screws are M5 x 35 and lid screws M3 x 30

added the adapter and ballast drawings. the tipping calculation is for a 5 N horizontal load at 225 mm above a flat bench, with all feet touching. it credits only conservative steel-block and rod weights. actual sliding resistance and holding force remain build-week checks

next: confirm connector and wire details, finish the supplier quotes and remaining tolerances, then review the parts in the slicer. no printing or physical testing this week

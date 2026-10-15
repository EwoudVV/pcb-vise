# prototype assembly

draft instructions for build week. nothing printed yet. start with the fit samples and one jaw clamp before making the whole set

## printing

the STLs in `exports/parts/` are oriented for printing and fit the P1S bed. keep them at 100% scale. the [Bambu Studio plate layouts](exports/print-plates/) include the materials and support settings

- use PLA for the first fit samples
- use PETG-CF for the rigid parts with the 0.4 mm hardened-steel nozzle
- use TPU for AMS for the friction rings, shoes, ballast liners and edge grips
- print the jaws with the adapter face down, so the rod bores run vertically
- print the carriers with their inner flat face down, and the pivot knobs with the washer face down
- print the TPU grips with the rail underside down
- print TPU shoes on their closed toe end so the retaining lips build vertically
- the right-hand base bars print top face down so their lap ledges rest on the plate
- the feet need supports under the bar-seat roofs. remove these through the side openings and clean out the nut pockets before assembly

## base

1. join each pair of base bars at the middle lap with two M4 x 12 screws and M4 nuts. the screw heads are on top and the nuts sit underneath. assemble this before fitting the feet
2. place the bars in the recesses on the inner halves of the feet. the upright's inner screws pass through the bars too
3. load the M5 nuts through the openings under the feet. fit each upright with four M5 x 35 screws and M5 washers
4. load the M3 lid nuts from underneath. deburr the four supplied-cut steel blocks and check that each is no longer than 63.17 mm. fit them in the TPU liners, then fit the four lids with eight M3 x 30 screws
5. slide the TPU shoes onto the ends of the feet. the lips hook over the base, and the recess inside leaves room for the lid screw

tighten by hand and keep the base joints flat. don't force a nut or rod into a hole that's too small

## rotating frame

1. load the two M6 x 50 hex bolts into the carriers from the inside. their heads sit in hex pockets and point their threaded ends outwards
2. insert both guide rods into one carrier, slide both jaws onto them, then fit the other carrier. the blind seats retain the rods once the frame is installed between the uprights
3. put a TPU friction ring between each carrier disc and upright
4. fit an M6 steel washer on the outside of each upright. load an M6 nut into each knob from the outer end, then thread the knobs onto the pivot bolts
5. loosen the knobs to turn the frame, then tighten both to hold it. test this with a light dummy board first

the rod seats leave 0.5 mm at each end. check the rod lengths before assembly. if the rods move end to end, add shims in the seats rather than bending the uprights inward

## jaws and edge grips

1. fit an M4 nut under each jaw clamp and an M4 x 50 screw with washer from above
2. insert the four M3 grip nuts through the outer faces of the jaw bodies
3. attach the TPU grips with four M3 x 20 screws, inserted from between the jaws. do this before moving the jaws together around a small board
4. seat the board edges in the V grooves, then bring the jaws into light contact and lock them with an Allen key. don't force the jaws in or bend the board
5. check that the grips miss the components and solder joints. leave about 3 mm clear along the held edges

start with a plain board. try 0.8, 1.6 and 2.4 mm boards when checking the printed grips. the grooves are intended to accept these thicknesses without swapping inserts

## optional ESC attachment

swap the TPU grips for the rigid mounting-hole adapters and use four M3 x 25 screws to attach them. the general-purpose grips' shorter screws are not used here

point the XT60 toward the unused rod length. put four M3 nuts under the adapter rails, then fit four M3 x 25 screws and small washers through the board holes. check that the heads and washers clear the components

## tests before use

- check the printed bores and nut pockets with the actual hardware
- test one split clamp on a rod before making the second
- verify all screws fully engage their nuts and no tip touches the bench
- test the TPU shoes for grip and retention
- test the pivot lock first with a light dummy board, then with representative board mass
- turn the board through a full rotation and check that components and cables clear the frame
- measure the assembled mass and test for tipping and sliding with gentle hand pressure

the base calculation is in [DESIGN.md](DESIGN.md). it hasn't been load-tested, and the calculation doesn't tell us whether the feet will slide

keep the PCB out of the holder for reflow. the printed parts are not a reflow fixture

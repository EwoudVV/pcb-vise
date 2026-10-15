# prototype assembly

these are draft instructions for build week. the design is still changing, and nothing has been printed or tested yet. when the build starts, print the small fit samples and one jaw clamp before making the whole vise

## printing

the STLs in `exports/parts/` are already moved to the build plate and oriented. do not rescale them. all fit within the P1S's 256 mm envelope. the material and orientation for each part are recorded in `cad/mechanism-checks.json`

- PLA is suitable for the first dimensional samples
- PETG-CF is the candidate for the rigid parts. confirm a hardened-steel nozzle before using it
- TPU for AMS is for the two friction rings, four shoes and optional edge grips
- print the jaws with the adapter face down, so the rod bores run vertically
- print the carriers with their inner flat face down, and the pivot knobs with the washer face down
- print TPU shoes on their closed toe end so the retaining lips build vertically
- slice and inspect the captive-nut ceilings, rod-seat ceilings and horizontal screw holes. small bridges may need tuning; these orientations have not been tested on the printer

## base

1. join each pair of base bars at the middle lap with two M4 x 12 screws and M4 nuts. the screw heads are on top and the nuts sit underneath. assemble this before fitting the feet
2. place the bars in the recesses on the inner halves of the feet. the upright's inner screws pass through the bars too
3. load the M5 nuts through the openings under the feet. fit each upright with four M5 x 35 screws and M5 washers
4. load the M3 lid nuts from underneath. fit the four TPU liners and steel blocks, then fit the four lids with eight M3 x 30 screws
5. slide the TPU shoes onto the ends of the feet. their upper lips retain them on the base. the inside of each shoe has a blind relief for the outer lid-screw tip

hand-tighten fasteners and check that the lap joints stay flat. don't use screw torque to force an incorrectly sized nut or rod into a printed part

## rotating frame

1. load the two M6 x 50 hex bolts into the carriers from the inside. their heads sit in hex pockets and point their threaded ends outwards
2. insert both guide rods into one carrier, slide both jaws onto them, then fit the other carrier. the blind seats retain the rods once the frame is installed between the uprights
3. put a TPU friction ring between each carrier disc and upright
4. fit an M6 steel washer on the outside of each upright. load an M6 nut into each knob from the outer end, then thread the knobs onto the pivot bolts
5. adjust both knobs until the frame turns when loosened and holds when tightened. this friction lock still needs a physical holding test

the nominal rod seats allow 0.5 mm at each rod end. check actual shaft length before assembly. shim the blind seats if there is noticeable axial movement; don't bow the uprights to remove it

## jaws and adapters

1. fit an M4 nut under each jaw clamp and an M4 x 50 screw with washer from above. the horizontal slit lets the jaw close around the front guide rod. an Allen key is used for this lock
2. insert the four M3 adapter nuts through the outer faces of the jaw bodies
3. choose either the raised ESC adapters or the TPU edge grips. the edge grips hold boards at the original pivot-axis height; use the separate edge-grip assembly file to view that setup. fasten them with the same four M3 x 25 screws, inserted from the space between the jaws
4. attach the inserts before closing the jaws around a small board. at the minimum opening, there is not enough room between them to insert a long driver
5. for the ESC, turn the board so the XT60 points toward the unused rod length. load the four M3 nuts beneath its raised adapter rails, then use four M3 x 25 screws and small washers through the PCB mounting holes. the posts raise the board 10 mm above the original position. confirm the washer and screw-head clearance on the populated board
6. for the TPU edge grips, slide the jaws into light contact with the board and lock their positions. the nominal grooves are 2.2 mm high for a 1.6 mm board. don't squeeze or bend the PCB

## tests before use

- check the printed bores and nut pockets with the actual hardware
- test one split clamp on a rod before making the second
- verify all screws fully engage their nuts and no tip touches the bench
- test the TPU shoes for grip and retention
- test the pivot lock first with a light dummy board, then with representative board mass
- check full rotation with actual component heights and cables; the CAD review includes the available component models and reserved connector spaces; the missing models and actual wiring still need confirmation
- measure the assembled mass and test for tipping and sliding with gentle hand pressure

the revised base uses 240 mm feet and four steel blocks in lined pockets. its calculated tipping margin is just over 1.5 for a 5 N horizontal force at 225 mm height, using conservative block and rod weights. the calculation assumes a level bench and all feet touching. it does not establish sliding resistance or cover impacts

keep the PCB out of the holder for reflow. the printed parts are not a reflow fixture

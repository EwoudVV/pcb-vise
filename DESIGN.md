# design notes

this is a general-purpose pcb vise. the main model uses edge grips. the ESC mounting-hole adapters are an optional attachment

## board range

- rectangular boards 30-160 mm wide and 30-160 mm deep
- board thicknesses from 0.8 to 2.4 mm
- about 3 mm of clear edge where the grips touch

the V grooves centre the board as the jaws move in. the grips lift it 10 mm above the pivot axis. narrower mounting rails and M3 x 20 screws leave more room underneath

checked space for components up to 25 mm above and 10 mm below the board, inside that 3 mm edge margin. the underside tip-access check starts 9 mm in from the held edges. connectors that stick beyond the outline still need checking against the particular board

these are CAD checks. print a grip pair and try actual boards during build week before treating the range as proven

## base and printing

the jaws slide on two 8 x 250 mm rods and lock with M4 screws. M6 bolts and knobs hold the angle

the feet are 240 mm long, with four steel blocks in TPU liners. the tipping calculation gives a margin just over 1.5 for a 5 N sideways force at 225 mm above a flat bench, with all feet touching. sliding still needs testing

the P1S has a 0.4 mm hardened-steel nozzle. the saved plates use PETG-CF for the rigid parts and TPU for AMS for the soft parts. the feet use supports, and the right base bars print top face down

## before submission

- finish the rod shipping quote and arrange the steel cuts
- review the drawings and build-week fit samples
- fill out the website BOM, take the final cart screenshots and make the closing reel

## build week

start with the rod and nut samples, one jaw clamp and the edge grips. try thin and thick boards, then adjust the fits before printing everything. check the pivot lock, feet and base stability with a board fitted

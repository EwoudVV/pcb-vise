# design notes

this week is for the design. printing and testing come during build week

## where it's at

the jaws slide on two 8 x 250 mm rods. M4 screws lock them in place, and the knobs at either end lock the rotation. the base has steel weights inside and TPU covers on the feet

there are two sets of grips: mounting-hole adapters for my ESC, and slotted TPU grips for other boards. the ESC adapters lift it 10 mm, with the XT60 facing the unused length of the rods. some connector models were missing, so i left extra space around them. the real connector sizes and cable bends still need checking

the feet are now 240 mm long. four steel blocks sit in TPU liners inside them. the tipping calculation gives a margin just over 1.5 for a 5 N sideways force at 225 mm above a flat bench, with all four feet touching. it only counts the steel blocks and rods. whether the feet slide still needs testing

the current model is [pcb-vise.FCStd](cad/pcb-vise.FCStd). the [edge-grip version](cad/pcb-vise-edge-grips.FCStd) holds boards at the original height. files with `layout` in the name are from the first version

## before submission

- confirm the remaining connector sizes and cable clearance
- check the clamp walls, screw lengths, nut access and print allowances
- finish the drawings and price the hardware, including shipping
- check supports, bridges and part orientation in Bambu Studio
- fill out the website BOM, take cart screenshots and make the closing reel

## sizes and materials

aiming for boards 30-160 mm wide and up to 160 mm across the rotating frame. the model uses a 1.6 mm board. the ESC mounting holes are 109 x 105 mm apart

i have a P1S, PLA, PETG-CF and TPU for AMS. still need to confirm the hardened nozzle for PETG-CF. screw sizes and quantities are in [HARDWARE.md](HARDWARE.md)

## build week

start with the rod and nut fit samples, then one jaw clamp. adjust the fits before printing everything. once it's assembled, check that the pivot holds, the feet stay on, and the base doesn't slide or tip with a board in it

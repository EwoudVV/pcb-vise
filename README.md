# pcb vise

[Half Life project](https://halflife.hackclub.com/projects/cmv5uxwy90kuh01n00i6f4u88)

i'm making a pcb vise for soldering. the jaws slide to fit different boards, and the whole frame flips over so i can get to the back without taking the board out

![pcb vise](exports/mechanisms-preview.png)

this is for Half Life CAD week. still designing it, nothing printed yet

## how it works

the jaws slide on two steel rods and lock with an Allen key. the knobs on either side hold the frame at the angle i want

the grips bolt on, so i can swap between:

- an adapter that uses the four mounting holes on my ESC
- TPU grips with slots for the edges of other boards

my ESC has too much stuff near the edges for normal grips. the adapters use its mounting holes and raise it a little to leave room for the connectors

![jaw and mounting adapter](exports/jaw-detail.png)

steel blocks inside the feet add weight to the base. TPU covers go on the ends for grip. the base screws together from smaller pieces that fit on my P1S

## materials

planning on PETG-CF for the rigid parts, TPU for AMS for the soft parts, and PLA for the first fit samples. the rods and fasteners are metal

## files

- [FreeCAD model](cad/pcb-vise.FCStd)
- [edge-grip assembly](cad/pcb-vise-edge-grips.FCStd)
- [STEP file](exports/pcb-vise.step)
- [STL files](exports/parts/) and [Bambu Studio plates](exports/print-plates/)
- [adapter drawing](drawings/esc-adapter.svg) and [feet and ballast drawing](drawings/feet-and-ballast.svg)
- [hardware list](HARDWARE.md) and [CSV](hardware.csv)
- [assembly instructions](ASSEMBLY.md), still being worked on

## still to finish

- check the remaining connector sizes and room for cables
- finish the fits and drawings
- finish the shipping quotes and arrange cutting the steel
- finish the submission BOM and media

printing and testing come during build week

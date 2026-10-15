# pcb vise

[Half Life project](https://halflife.hackclub.com/projects/cmv5uxwy90kuh01n00i6f4u88)

i'm making a pcb vise for soldering. the jaws slide to fit different boards, and the whole frame flips over so i can get to the back without taking the board out

![pcb vise](exports/mechanisms-preview.png)

this is for Half Life CAD week. nothing printed yet

## how it works

the jaws slide on two steel rods and lock with an Allen key. the knobs on either side hold the frame at the angle i want

the TPU grips have V-shaped grooves, so the same pair can hold different board thicknesses. they sit above the jaws to leave more room for components and soldering underneath

![edge grip](exports/jaw-detail.png)

the current design is for rectangular boards 30-160 mm wide, 30-160 mm deep and 0.8-2.4 mm thick. leave about 3 mm clear along the edges being held. the fit and holding force still need checking with printed parts

there's also an optional mounting-hole adapter for my ESC. it swaps onto the same jaws when a board's edges are too crowded for grips

steel blocks inside the feet add weight to the base. TPU covers go on the ends for grip. the base screws together from smaller pieces that fit on my P1S

## materials

planning on PETG-CF for the rigid parts, TPU for AMS for the soft parts, and PLA for the first fit samples. the rods and fasteners are metal

## files

- [FreeCAD model](cad/pcb-vise.FCStd)
- [optional ESC assembly](cad/pcb-vise-esc.FCStd)
- [STEP file](exports/pcb-vise.step)
- [STL files](exports/parts/) and [Bambu Studio plates](exports/print-plates/)
- [grip drawing](drawings/edge-grip.svg) and [feet and ballast drawing](drawings/feet-and-ballast.svg)
- [hardware list](HARDWARE.md) and [CSV](hardware.csv)
- [assembly instructions](ASSEMBLY.md), still being worked on

## still to finish

- finish the submission journal and media
- print the fit samples during build week

printing and testing come during build week

# fit samples

start with `rod-and-nut-fit.stl` in PLA. print it flat with the holes vertical, at 100% scale. use the same wall and hole-compensation settings as the full parts

the corner notch marks the starting end of both rows. with that notch at the lower left:

| Row | Left to right |
| --- | --- |
| Round holes, nearest the notch | 8.1, 8.2, 8.3 and 8.4 mm diameter |
| Hex pockets | 10.1, 10.2, 10.3 and 10.4 mm across flats |

the hex pockets are 5.3 mm deep with 6.6 mm through-holes, for M6 DIN 934 nuts

try the rods and nuts you'll use in the vise. find a hole that slides without wobbling, and a pocket where the nut presses in by hand but can't turn. don't hammer them in

once a size looks right, try it in the final material too. a good fit in PLA may change in PETG-CF. the clamp and pivot still need their own tests

## M3, M4 and M5 pockets

`m3-m4-m5-fit.stl` checks the smaller nuts. keep the corner notch at the lower left. the rows from that edge are M3, M4 and M5. each row has two pockets:

| Nut | Left pocket AF | Right pocket AF | Pocket depth |
| --- | ---: | ---: | ---: |
| M3 | 5.7 mm | 5.8 mm | 2.8 mm |
| M4 | 7.2 mm | 7.3 mm | 3.6 mm |
| M5 | 8.2 mm | 8.3 mm | 4.4 mm |

the right-hand pockets match the current vise model. use the sizes in [the hardware list](../../HARDWARE.md), especially the 4 mm high M5 nut. adjust the pockets if the samples don't fit

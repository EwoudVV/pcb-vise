# rod and nut fit sample

print `rod-and-nut-fit.stl` flat in PLA first. the coupon is 62 x 46 x 8 mm. keep the holes vertical and use the same perimeter and hole-compensation settings planned for the parts. don't resize it in the slicer

the corner notch marks the starting end of both rows. with that notch at the lower left:

| Row | Left to right |
| --- | --- |
| Round holes, nearest the notch | 8.1, 8.2, 8.3 and 8.4 mm diameter |
| Hex pockets | 10.1, 10.2, 10.3 and 10.4 mm across flats |

the hex pockets are 5.3 mm deep with 6.6 mm through-holes. they're for checking the fit of M6 DIN 934 nuts, not for cutting a thread in plastic

try the actual rods and nuts you plan to use. record which rod hole slides without sticking or excessive play, and which nut pocket seats with light hand pressure without rotating. don't hammer parts into the sample

this only checks fits. it doesn't test clamp force, friction, layer strength or the complete vise. repeat the useful hole and pocket sizes in the final structural material before printing all the parts. changing material or print orientation can change the fit

## M3, M4 and M5 pockets

`m3-m4-m5-fit.stl` is a second, 50 x 50 x 8 mm coupon. keep the corner notch at the lower left. the rows from that edge are M3, M4 and M5. each row has two pockets:

| Nut | Left pocket AF | Right pocket AF | Pocket depth |
| --- | ---: | ---: | ---: |
| M3 | 5.7 mm | 5.8 mm | 2.8 mm |
| M4 | 7.2 mm | 7.3 mm | 3.6 mm |
| M5 | 8.2 mm | 8.3 mm | 4.4 mm |

the right-hand sizes match the current mechanism model. use the nut dimensions in HARDWARE.md, especially the 4 mm high M5 nut. these are printed fit allowances, not promises about your printer's output

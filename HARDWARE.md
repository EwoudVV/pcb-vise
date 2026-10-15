# hardware for one vise

quantities below come from the assembly model. they include the ESC adapters. the TPU edge grips reuse the four adapter screws and nuts. mounting the ESC uses another four screws, four washers and four nuts; leave those out when using ordinary edge grips

this is a size and quantity BOM, not a priced order. the two guide rods had a $24.06 combined reference price on October 12, before shipping. other prices still need checking

| Part | Qty |
| --- | ---: |
| M5 x 35 socket cap screw DIN 912 | 8 |
| M5 washer, 10 mm OD x 1 mm | 8 |
| M5 nut DIN 934, 8 mm AF x 4 mm | 8 |
| M3 x 30 socket cap screw DIN 912 | 8 |
| M3 nut DIN 934, 5.5 mm AF x 2.4 mm | 16 |
| M4 x 12 socket cap screw DIN 912 | 4 |
| M4 nut DIN 934, 7 mm AF x 3.2 mm | 6 |
| M6 x 50 hex bolt DIN 933 | 2 |
| M6 washer, 12 mm OD x 1.6 mm | 2 |
| M6 nut DIN 934, 10 mm AF x 5 mm | 2 |
| 8 x 250 mm smooth steel rod | 2 |
| M4 x 50 socket cap screw DIN 912 | 2 |
| M4 washer, 9 mm OD x 1 mm | 2 |
| M3 x 25 socket cap screw DIN 912 | 8 |
| M3 washer, 6.4 mm OD x 0.5 mm | 4 |
| Steel ballast, 38.1 x 60 x 19.05 mm | 4 |

## fit details

- use ordinary DIN 934 full nuts. Nyloc nuts and some ISO 4032 nuts are taller than these pockets
- M3 nuts: 5.5 mm across flats, 2.4 mm high; pockets are 5.8 mm across flats
- M4 nuts: 7 mm across flats, 3.2 mm high; pockets are 7.3 mm across flats
- M5 nuts: 8 mm across flats, 4 mm high; the 4.4 mm pockets do not accept a 4.7 mm tall substitute
- M6 nuts: 10 mm across flats, 5 mm high; knob pockets are 10.3 mm across flats
- check the actual rod diameter and nut fit with small samples before printing everything

the screw models use plain cylinders for the threads and simplified heads. their lengths are measured from under the head. verify the ordered hardware against the dimensions above

## printed and loose parts

the STL directory contains 32 printed parts: 30 for the ESC configuration and two alternative TPU edge grips. the TPU friction rings and slip-on feet are included. four steel blocks sit in TPU liners under the ballast lids

the ballast is four pieces of 3/4 x 1 1/2 inch steel bar, each cut to 60 mm. the nominal dimensions are 38.1 x 60 x 19.05 mm. order them cut or arrange cutting during build week, then deburr the edges before fitting the liners

a 12 inch length of [1018 bar](https://www.onlinemetals.com/en/buy/carbon-steel/0-75-x-1-5-carbon-steel-rectangle-bar-1018-cold-finish/pid/9720) was listed at $19.66 on October 15. that covers the stock length for four pieces with cutting allowance, but not cutting charges or shipping. the blocks are about 1.36 kg together by calculation

the stability calculation uses smaller dimensions and credits only the blocks and rods. it assumes a flat bench, all four feet touching, and a 5 N horizontal load no higher than 225 mm. it gives a tipping margin just over 1.5. this is a design case, not a tested rating; sliding friction still needs checking during build week

see [the ballast drawing](drawings/feet-and-ballast.svg) for the cut lengths, pockets and lid dimensions

## references

- [DIN 934 nut dimensions](https://www.westfieldfasteners.co.uk/Standards/Nut_Hex_M.html)
- [DIN 912 cap screw dimensions](https://www.boltking.co.uk/din-912)
- [guide rod reference](https://abra-electronics.com/robotics/axles-rods/mp-rm8-250-8mm-m8-250mm-linear-shaft-rail-rod.html)

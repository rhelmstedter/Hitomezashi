#!python3
import random

HEIGHT = 30
WIDTH = 30

vs_grid = []
vs_oddrow = []
vs_evenrow = []
hs_grid = []
hs_oddrow = []
hs_evenrow = []

# contruct veritcal stiches randomly for first row and opposite for second row.
for stitch in range(WIDTH):
    if random.randint(0, 1) == 1:
        vs_oddrow.append('|')
        vs_evenrow.append(' ')
    else:
        vs_oddrow.append(' ')
        vs_evenrow.append('|')


# construct nested lists of all vertical stitches
for row in range(HEIGHT):
    if row % 2 == 0:
        vs_grid.append(vs_evenrow)
    else:
        vs_grid.append(vs_oddrow)

# construct horizontal stitches
while len(hs_oddrow) < WIDTH:
    hs_oddrow.append('__')
    hs_oddrow.append('  ')

while len(hs_evenrow) < WIDTH:
    hs_evenrow.append('  ')
    hs_evenrow.append('__')

# construct nested lists of all horizontal stitches
for row in range(HEIGHT):
    if random.randint(0, 1) == 0:
        hs_grid.append(hs_evenrow)
    else:
        hs_grid.append(hs_oddrow)

# print out the horizontal and vertical stitches together
print("___"*WIDTH)
for vs, hs in zip(vs_grid, hs_grid):
    for stitch in range(WIDTH):
        print(vs[stitch]+hs[stitch], end='')
    print()
print("___"*WIDTH)

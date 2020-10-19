#! python3
import random

HEIGHT = 30
WIDTH = 30

vgrid = []
vodd = []
veven = []
hgrid = []
hodd = []
heven = []

# contruct veritcal stiches
for x in range(WIDTH):
    if random.randint(0, 1) == 1:
        vodd.append('|')
        veven.append(' ')
    else:
        vodd.append(' ')
        veven.append('|')

# construct nested lists of all vertical stitches
for y in range(HEIGHT):
    if y % 2 == 0:
        vgrid.append(veven)
    else:
        vgrid.append(vodd)

# construct horizontal stitches
while len(hodd) < WIDTH:
    hodd.append('__')
    hodd.append('  ')

while len(heven) < WIDTH:
    heven.append('  ')
    heven.append('__')

# construct nest lists of all horizontal stitches
for y in range(HEIGHT):
    if random.randint(0, 1) == 0:
        hgrid.append(heven)
    else:
        hgrid.append(hodd)

# print out the horizontal and vertical stitches together
print("___"*WIDTH)
for v, h in zip(vgrid, hgrid):
    for i in range(WIDTH):
        print(v[i]+h[i], end='')
    print()
print("___"*WIDTH)

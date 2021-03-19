#!python3

binary = {
    "A": "01000001",
    "B": "01000010",
    "C": "01000011",
    "D": "01000100",
    "E": "01000101",
    "F": "01000110",
    "G": "01000111",
    "H": "01001000",
    "I": "01001001",
    "J": "01001010",
    "K": "01001011",
    "L": "01001100",
    "M": "01001101",
    "N": "01001110",
    "O": "01001111",
    "P": "01010000",
    "Q": "01010001",
    "R": "01010010",
    "S": "01010011",
    "T": "01010100",
    "U": "01010101",
    "V": "01010110",
    "W": "01010111",
    "X": "01011000",
    "Y": "01011001",
    "Z": "01011010",
    "a": "01100001",
    "b": "01100010",
    "c": "01100011",
    "d": "01100100",
    "e": "01100101",
    "f": "01100110",
    "g": "01100111",
    "h": "01101000",
    "i": "01101001",
    "j": "01101010",
    "k": "01101011",
    "l": "01101100",
    "m": "01101101",
    "n": "01101110",
    "o": "01101111",
    "p": "01110000",
    "q": "01110001",
    "r": "01110010",
    "s": "01110011",
    "t": "01110100",
    "u": "01110101",
    "v": "01110110",
    "w": "01110111",
    "x": "01111000",
    "y": "01111001",
    "z": "01111010",
}

plain_text = input("What do you want to stitch? ")

binary_text = ""
for letter in plain_text:
    binary_code = binary.get(letter)
    binary_text += binary_code

vgrid = []
vodd =[]
veven = []
hgrid = []
hodd = []
heven = []

# contruct veritcal stiches for first two rows
for char in binary_text:
    if int(char) == 1:
        veven.append("|")
        vodd.append(" ")
    else:
        veven.append(" ")
        vodd.append("|")

# construct nested lists of all vertical stitches with the first two rows alternating
for row in range(len(binary_text)):
    if row % 2 == 0:
        vgrid.append(veven)
    else:
        vgrid.append(vodd)

# construct horizontal stitches for 0 and 1 pattern
while len(hodd) < len(binary_text):
    hodd.append("__")
    hodd.append("  ")

while len(heven) < len(binary_text):
    heven.append("  ")
    heven.append("__")

# construct nested lists of all horizontal stitches
for char in binary_text:
    if int(char) == 0:
        hgrid.append(heven)
    else:
        hgrid.append(hodd)

# print out the horizontal and vertical stitches together
print("This is a hitomezashi pattern based on " + plain_text + ".")
print()
print("___" * len(binary_text))
for v, h in zip(vgrid, hgrid):
    for i in range(len(binary_text)):
        print(v[i] + h[i], end="")
    print()
print("___" * len(binary_text))

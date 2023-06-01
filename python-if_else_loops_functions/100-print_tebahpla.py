#!/usr/bin/python3
txt = "{}"
rettel = 122
for i in range(97, 123):
    letter = rettel
    if (i % 2 == 0):
        letter = letter - 32
    print(txt.format(chr(letter)), end="")
    rettel = rettel - 1

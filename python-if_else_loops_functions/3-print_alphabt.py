#!/usr/bin/python3
txt = "{}"
for i in range(97, 123):
    if (i != 101 and i != 113):
        print(txt.format(chr(i)), end="")

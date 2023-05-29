#!/usr/bin/python3
txt = "{} = {}\n"
for i in range(0, 99):
    hd = hex(i)
    print(txt.format(i, hd), end="")

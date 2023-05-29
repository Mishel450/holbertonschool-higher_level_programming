#!/usr/bin/python3
txt = "{}"
for i in range(0, 100):
    n = i
    if (n < 10):
        n = f"0{n}"
    if (i != 99):
        print(txt.format(n), end=", ")
    else:
        print(txt.format(n))

#!/usr/bin/python3
a = 1
b = a
txt = "{}{}"
for i in range(0, 10):
    b = a
    for j in range(a, 10):
        print(txt.format(i, b), end="")
        if (i != 8 and a != 9):
            print(", ", end="")
        else:
            print("", end="\n")
        b = b + 1
    a = a + 1

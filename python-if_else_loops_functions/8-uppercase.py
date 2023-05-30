#!/usr/bin/python3
txt = "{}"
def uppercase(str):
    for i in range(0, len(str)):
        letter = ord(str[i])
        if (letter >= 97 and letter <= 122):
            letter = letter - 32
        if (i == len(str) - 1):
            print(txt.format(chr(letter)), end="\n")
        else:
            print(txt.format(chr(letter)), end="")

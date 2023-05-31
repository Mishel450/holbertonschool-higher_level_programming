#!/usr/bin/python3
def uppercase(str):
    txt = "{}"
    for i in range(0, len(str)):
        letter = ord(str[i])
        if (letter >= 97 and letter <= 122):
            letter = letter - 32
        print(txt.format(chr(letter)), end="")
    print("", end="\n")

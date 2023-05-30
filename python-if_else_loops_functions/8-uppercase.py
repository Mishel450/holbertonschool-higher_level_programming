#!/usr/bin/python3
txt = "{}"
def uppercase(str):
    for i in range(0, len(str)):
        letter = ord(str[i])
        if (letter >= 97 and letter <= 122):
            print(txt.format(32 + str[i]), end="")
        else:
            print(txt.format(str[i]), end="")

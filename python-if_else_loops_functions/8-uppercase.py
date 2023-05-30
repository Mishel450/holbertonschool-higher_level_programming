#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        letter = ord(str[i])
        if (letter >= 97 and letter <= 122):
            str[i] = 32 + str[i]

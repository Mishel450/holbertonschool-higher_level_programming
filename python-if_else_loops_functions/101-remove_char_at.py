#!/usr/bin/python3
def remove_char_at(str, n):
    txt = "{}"
    for i in range(0, len(str)):
        if (str[i] != n):
            print(txt.format(str[i]), end="")

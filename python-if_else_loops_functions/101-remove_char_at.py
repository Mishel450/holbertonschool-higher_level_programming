#!/usr/bin/python3
def remove_char_at(str, n):
    txt = "{}"
    if (n >= 0):
        for i in range(0, len(str)):
            if (i == n):
                str = str.replace(str[i], '')
    return (str)

#!/usr/bin/python3
def print_last_digit(number):
    txt = "{}"
    if (number < 0):
        number = number * -1
    lastD = number % 10
    print(txt.format(lastD), end="")
    return (lastD)

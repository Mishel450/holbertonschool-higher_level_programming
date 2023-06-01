#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    txt = "{} {} {} = {}"
    a = 10
    b = 5
    print(txt.format(a, "+", b, add(a, b)))
    print(txt.format(a, "-", b, sub(a, b)))
    print(txt.format(a, "*", b, mul(a, b)))
    print(txt.format(a, "/", b, div(a, b)))

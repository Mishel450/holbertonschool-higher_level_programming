#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    txt = "{} + {} = {}"
    a = 1
    b = 2
    c = add(a, b)
    print(txt.format(a, b, c))

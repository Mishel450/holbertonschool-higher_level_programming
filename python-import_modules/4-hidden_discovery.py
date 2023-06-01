#!/usr/bin/python3
if __name__ == "__main__":
    txt = "{}"
    import hidden_4
    a = (dir(hidden_4))
    b = (dir(hidden_4))
    for i in a:
        if (i[0] == "_"):
            b.remove(i)
    for j in b:
        if (j != 0):
            print(txt.format(j))

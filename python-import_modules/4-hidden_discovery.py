#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = (dir(hidden_4)) 
    b = (dir(hidden_4))
    for i in a:
        if (i[0] == "_"):
            b.remove(i)
    print(b)

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    txtarguments = "{} {}:"
    txt = "{}: {}"
    if (len(argv) - 1 == 1):
        print(txtarguments.format(len(argv) - 1, "argument"))
    else:
        print(txtarguments.format(len(argv) - 1, "arguments"))
    for i in range(1, len(argv)):
        print(txt.format(i, argv[i]))

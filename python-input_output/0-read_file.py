#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        file_read = file.read()
        return(print((file_read), end=""))

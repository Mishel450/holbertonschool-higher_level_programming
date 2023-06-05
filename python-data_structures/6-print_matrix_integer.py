#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    txt = "{:d}"
    for i in matrix:
        for j in i:
            print(txt.format(j), end=" ")
        print()

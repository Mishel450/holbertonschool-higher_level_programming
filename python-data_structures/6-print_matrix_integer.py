#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    txt = "{:d}"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i != len(matrix) and j != len(matrix[i]) - 1):
                print(txt.format(matrix[i][j]), end=" ")
            else:
                print(txt.format(matrix[i][j]), end="")
        print()

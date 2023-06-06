#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix.copy()
    for i in range(len(a)):
        a[i] = list(map(lambda j: j * j, matrix[i]))
    return (a)

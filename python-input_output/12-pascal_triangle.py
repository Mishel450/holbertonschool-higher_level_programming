#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing the Pascal’s
    triangle of n:
    *Returns an empty list if n <= 0
    *You can assume n will be always an integer"""

    lis = []
    if n <= 0:
        return []

    for a in range(n):
        fila = [1]
        for s in range(a):
            if s == a - 1:
                fila.append(1)
            else:
                fila.append(lis[a - 1][s + 1] + lis[a - 1][s])
        lis.append(fila)
    return lis

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    j = 0
    if (len(tuple_a) >= 2):
        i = i + tuple_a[0]
        j = j + tuple_a[1]
    if (len(tuple_b) >= 2):
        i = i + tuple_b[0]
        j = j + tuple_b[1]
    if (len(tuple_a) == 1):
        i = i + tuple_a[0]
    if (len(tuple_b) == 1):
        i = i + tuple_b[0]
    if (tuple_a == 0):
        i = i + 0
    if (tuple_b == 0):
        i = i + 0
    zero = i
    one = j
    my_tuple = (zero, one)
    return (my_tuple)

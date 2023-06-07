#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for i in a:
        a_value = a.get(i)
        a_value *= 2
        a.update({i: a_value})
    return (a)

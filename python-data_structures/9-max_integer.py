#!/usr/bin/python3
def max_integer(my_list=[]):
    txt = "{:d}"
    if (my_list is None):
        return (None)
    my_list.sort()
    return (txt.format(my_list[-1]))

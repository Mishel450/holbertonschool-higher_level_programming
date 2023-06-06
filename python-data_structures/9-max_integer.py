#!/usr/bin/python3
def max_integer(my_list=[]):
    txt = "{:d}"
    if (len(my_list) > 0):
        my_list.sort()
        return (txt.format(my_list[-1]))
    else:
        return (None)

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list):
        txt = "{:d}"
        my_list.reverse()
        for i in range(0, len(my_list)):
            print(txt.format(my_list[i]))

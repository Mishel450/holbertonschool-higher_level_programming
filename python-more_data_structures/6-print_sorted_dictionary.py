#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    txt = "{}: {}"
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    a_dictionary = {i: a_dictionary[i] for i in myKeys}
    for key, value in a_dictionary.items():
        print(txt.format(key, value))

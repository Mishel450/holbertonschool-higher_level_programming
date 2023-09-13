#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary != None):
        a = a_dictionary.copy()
        sorted(a)
        key_list = list(a.keys())
        return (a[-1])
    else:
        return (None)

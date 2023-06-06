#!/usr/bin/python3
def search_replace(my_list, search, replace):
    counts = my_list.count(search)
    the_list = my_list.copy()
    for i in range(counts):
        found = the_list.index(search)
        the_list[found] = replace
    return (the_list)

#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            a = a + my_string[i]
    return (a)

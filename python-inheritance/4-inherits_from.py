#!/usr/bin/python3
"""4-task"""


def inherits_from(obj, a_class):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if (type(obj) != a_class and isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
#!/usr/bin/python3
"""3-task"""


def is_kind_of_class(obj, a_class):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
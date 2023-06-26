#!/usr/bin/python3
"""0-task"""


class Base:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    __nb_objects = 0
    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

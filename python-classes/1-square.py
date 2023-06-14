#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
module
"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Square
    """
    def __init__(self, __size=None):
        """python3 -c 'print(__import__("my_module").__doc__)'
        init the __size variable
        """
        self.__size = __size

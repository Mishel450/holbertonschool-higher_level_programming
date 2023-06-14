#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
module
"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Square
    """
    def __init__(self, __size=0):
        """python3 -c 'print(__import__("my_module").__doc__)'
        init the __size variable
        """
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

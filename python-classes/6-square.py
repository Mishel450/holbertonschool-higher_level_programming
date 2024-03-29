#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
module
"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Square
    """

    def __init__(self, __size=0, __position=(0, 0)):
        """python3 -c 'print(__import__("my_module").__doc__)'
        init
        """
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
        self.__position = __position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value
    
    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size > 0):
            for i in range(self.__size):
                for j in range(self.__size + self.__position):
                    if (i <= self.__position):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        elif (self.__size == 0):
            print()

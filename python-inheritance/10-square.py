#!/usr/bin/python3
"""10-task"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

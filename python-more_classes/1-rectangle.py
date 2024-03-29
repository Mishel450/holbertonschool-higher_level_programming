#!/usr/bin/python3
"""task-1"""


class Rectangle():
    """rectangle class"""

    def __init__(self, width=0, height=0):
        if not type(width) == int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not type(height) == int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

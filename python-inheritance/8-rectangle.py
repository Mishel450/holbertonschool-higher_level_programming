#!/usr/bin/python3
"""8-task"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, width, height):

        self.integer_validation("width", width)
        self.integer_validation("height", height)
        self.__width = width
        self.__height = height
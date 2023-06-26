#!/usr/bin/python3
from models.base import Base
"""2-task"""


class Rectangle(Base):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__width = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

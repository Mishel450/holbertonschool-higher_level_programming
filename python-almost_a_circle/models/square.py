#!/usr/bin/python3
"""10-task"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.__x, self.__y, self.__height))
    
    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.size = value

#!/usr/bin/python3
"""task 11"""


class Student:
    """task"""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attr = {}
        if not isinstance(attrs, list):
            return self.__dict__
        for a in attrs:
            if a in self.__dict__:
                attr[a] = self.__dict__[a]
        return attr

    def reload_from_json(self, json):
        for chiave, valore in json.items():
            setattr(self, chiave, valore)

#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_create_class(self):
        base1 = Base()
        self.assertAlmostEqual(base1.id, 2)
        base2 = Base()
        self.assertAlmostEqual(base2.id, 3)
        base3 = Base(22)
        self.assertAlmostEqual(base3.id, 22)
        base4 = Base(-22)
        self.assertAlmostEqual(base4.id, -22)

    def test_ToJsonString(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertAlmostEqual(Base.to_json_string([]), "[]")

    def test_SaveToFile(self):
        Base.save_to_file(None)
        self.assertAlmostEqual(os.path.exists("Base.json"), True)

    def test_FromJsonString(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(
            Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])

    def test_Update(self):
        r1_dictionary = {"id": 10, "width": 10, "height": 10}
        r1 = Rectangle.create(**r1_dictionary)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (10) 0/0 - 10/10")


if __name__ == "__main__":
    unittest.main()
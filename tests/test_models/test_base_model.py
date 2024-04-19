#!/usr/bin/python3
"""This is the base_model test module."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the base class module."""

    def setUp(self):
        """sets up all the required items for objects to work."""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        obj_dict = {"one":1, "two":2, "three":3}

    def test_uuid(self):
        """This method tests the id attribute."""
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertTrue(hasattr(self.obj1, "id"))
        self.asserIsInstance(self.obj1.id, str)
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_str_method(self):
        """Tests the str method."""
        self.assertEqual(str(self.obj1),\
                f"[BaseModel] ({self.obj1.id}) {self.obj1.__dict__}")
        self.assertEqual(str(self.obj2),\
                f"[BaseModel] ({self.obj1.id}) {self.obj1.__dict__}")

    def test_save(self):
        """Tests the save method."""
        self.assertIs(self.obj1.updated_at, None)
        self.obj1.save()
        self.assertIsNot(self.obj1.updated_at, None)

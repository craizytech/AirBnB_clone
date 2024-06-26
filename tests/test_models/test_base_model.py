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
        self.assertIsInstance(self.obj1.id, str)
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_str_method(self):
        """Tests the str method."""
        self.assertEqual(str(self.obj1),\
                f"[BaseModel] ({self.obj1.id}) {self.obj1.__dict__}")
        self.assertEqual(str(self.obj2),\
                f"[BaseModel] ({self.obj2.id}) {self.obj2.__dict__}")

    def test_save(self):
        """Tests the save method."""
        initial_updated = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(self.obj1.updated_at, initial_updated)

    def test_to_dict(self):
        """ Tests the to_dict() method in test_base_model."""
        self.object_dict = self.obj1.to_dict().copy()
        self.assertIsInstance(self.object_dict, dict)
        self.assertIsInstance(self.object_dict['created_at'], str)

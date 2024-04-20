#!/usr/bin/python3
"""The file storage test module."""
import unittest
import json
import os
import os.path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing the file storage module."""

    def setUp(self):
        """Sets up all the objects needed for testing"""
        self.f1_obj = FileStorage()
        self.f2_obj = FileStorage()
        self.b1_obj = BaseModel()
        self.b2_obj = BaseModel()
        self.test_file_path = "test_file.json"

    def test_instance(self):
        """Tests the instance of FileStorage."""
        self.assertIsInstance(self.f1_obj, FileStorage)

    def test_attributes(self):
        """Tests the private class attributes of the class."""
        with self.assertRaises(AttributeError):
            self.f1_obj.file_path
        with self.assertRaises(AttributeError):
            self.f1_obj.objects

        self.assertEqual(self.f1_obj._FileStorage__file_path, "file.json")
        self.assertIsNot(self.f1_obj._FileStorage__objects, None)

    def test_all(self):
        """ Tests the all method"""
        self.assertIsInstance(self.f1_obj._FileStorage__objects, dict)

    def test_new(self):
        """Tests the new method."""
        self.f1_obj.new(self.b1_obj)
        key = f"{self.b1_obj.__class__.__name__}.{self.b1_obj.id}"
        # check if object is present in __objects
        self.assertIn(key, self.f1_obj._FileStorage__objects)
        # check if inserted object inserted into __objects is same as original
        self.assertIs(self.f1_obj._FileStorage__objects[key], self.b1_obj)

    def test_save(self):
        """Tests save method"""
        self.Base_1 = BaseModel()
        self.Base_2 = BaseModel()
        FileStorage._FileStorage__file_path = self.test_file_path
        FileStorage._FileStorage__objects["key1"] = self.Base_1
        FileStorage._FileStorage__objects["key2"] = self.Base_2

        self.f1_obj.save()
        # verify that the file test_file.json has been created
        self.assertTrue(os.path.exists(self.test_file_path))

        # read contents of the json file
        with open(self.test_file_path, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        # check that the saved data matches the objects in __objects
        self.assertEqual(saved_data["key1"], self.Base_1.to_dict())
        self.assertEqual(saved_data["key2"], self.Base_2.to_dict())

    def tearDown(self):
        """Cleans up after test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

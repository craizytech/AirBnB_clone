#!/usr/bin/python3
"""The file storage test module."""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing the file storage module."""

    def setUp(self):
        """Sets up all the objects needed for testing"""
        self.f1_obj = FileStorage()
        self.f2_obj = FileStorage()
        self.b1_obj = BaseModel()

    def test_instance(self):
        """Tests the instance of FileStorage."""
        self.assertIsInstance(self.f1_obj, FileStorage)

    def test_attributes(self):
        """Tests the private class attributes of the class."""
        with self.assertRaises(AttributeError):
            self.f1_obj.file_path
        self.assertEqual(self.f1_obj._FileStorage__file_path, "file.json")

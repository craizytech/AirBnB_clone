#!/usr/bin/python3
"""The file storage test module."""
import unittests
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage:
    """Testing the file storage module."""

    def setUp(self):
        """Sets up all the objects needed for testing"""
        f1_obj = FileStorage()
        f2_obj = FileStorage()
        b1_obj = BaseModel()

    def test_instance(self):
        """Tests the instance of FileStorage."""
        self.assertIsInstance(f1_obj, FileStorage)

    def test_attributes(self):
        """Tests the private class attributes of the class."""
        with self.assertRaises(AttributeError):
            f1_obj.file_path
        self.assertIsEqual(f1_0bj_FileStorage__file_path, "file.json")

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

    def test_all(self):
        """tests the all method."""
        self.assertIs(

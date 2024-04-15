#!/usr/bin/python3
"""File storage module."""
import json
import os
import os.path

class FileStorage:
    """This class serializes and deserializes instances to/from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """stores the object with key <obj class name>.id"""
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_name] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON filepath only if file exists."""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)

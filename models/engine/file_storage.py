#!/usr/bin/python3
"""FileStorage Module."""
import json
import os
import os.path


class FileStorage:
    """serializes(instances->JSONfile) && deserializes(JSONfile->instances)"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """ inserts into __objects the obj with key '<obj class name>.id'
        Args:
            obj (object): the instance to be inserted into the __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes the __objects to JSON file in the __file_path."""
        save_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(save_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects only if file path exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                from models.base_model import BaseModel
                saved_dict = json.load(file)
                for obj in saved_dict.values():
                    class_name = obj['__class__']
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))

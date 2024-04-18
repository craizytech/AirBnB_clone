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

        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key]= obj

    def save(self):

        dic_rep = { key:FileStorage.__objects[key].to_dict() for key in FileStorage.__objects.keys()}

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:

            try:
                
                json.dump(dic_rep,file)
            except json.JSONEncoder:

                pass

    def reload(self):

        if os.path.exists(FileStorage.__file_path):

            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:

                try:
                    from models.base_model import BaseModel

                    json_dict = json.load(file)

                    FileStorage.__objects = {key:BaseModel(**value) for key, value in json_dict.items()}

                except json.JSONDecodeError:
                    pass


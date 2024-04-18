#!/usr/bin/python3
"""Base Class Module."""
import json
import uuid
import datetime


class BaseModel:
    """This is the base class for the project."""
    def __init__(self):
        """Constructor method."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Prints the representation of the instance."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the public instance attribute with the
        current date and time."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all the attributes of the class."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = BaseModel.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict

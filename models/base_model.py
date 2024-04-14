#!/usr/bin/python3
"""This is the Base model of the AirBnB project."""
import uuid
import json
import datetime

class BaseModel:
    """This is the base class that all the other classes inherit from."""

    def __init__(self):
        """This is the constructor method of the class."""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now().isoformat())
        self.updated_at = str(datetime.datetime.now().isoformat())

    def __str__(self):
        """Prints the representation of the object."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with current datetime."""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary containing the attributes of the class."""
        dict_object = self.__dict__
        dict_object['__class__'] = BaseModel.__name__
        return dict_object

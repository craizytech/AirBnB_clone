#!/usr/bin/python3
"""This is the Base model of the AirBnB project."""
import uuid
import json
import datetime

class BaseModel:
    """This is the base class that all the other classes inherit from."""

    self.id = uuid.uuid4()
    self.created_at = datetime.datetime.now().isoformat()
    self.updated_at = None

    def __str__(self):
        """Prints the representation of the object."""
        return f"[Base] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with current datetime."""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary containing the attributes of the class."""
        dict_object = self.__dict__
        dict_object['__class__'] = BaseModel.__name__

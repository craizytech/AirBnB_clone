#!/usr/bin/python3
"""This is the Base model of the AirBnB project."""
import uuid
import json
import datetime
from models import storage

class BaseModel:
    """This is the base class that all the other classes inherit from."""

    def __init__(self, *args, **kwargs):
        """This is the constructor method of the class.
        Args:
            args (tuple): This is a tuple containg the variable num of args
            kwargs (dict): Containing the variable num of kw arguments
        """
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.datetime.fromisoformat(v)
                self.__dict__[k] = v

    def __str__(self):
        """Prints the representation of the object."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at with current datetime."""
        self.updated_at = datetime.datetime.now()
        storage.save(self)

    def to_dict(self):
        """Returns a dictionary containing the attributes of the class."""
        dict_object = self.__dict__
        dict_object['__class__'] = BaseModel.__name__
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()
        return dict_object

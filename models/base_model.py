#!/usr/bin/python3
"""Base Class Module."""
import json
import uuid
import datetime


class BaseModel:
    """This is the base class for the project."""
    def __init__(self, *args, **kwargs):
        """Constructor method.
        Args:
            args (tuple): contains the variable num of args
            kwargs (dict): contains the dictionary attributes of an instance
        """
        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.datetime.fromisoformat(v)
                self.__dict__[k] = v

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

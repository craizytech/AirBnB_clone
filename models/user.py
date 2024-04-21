#!/usr/bin/python3
"""User Module."""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class User(BaseModel):
    """Class User defines attributes of a user and is subclass of BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


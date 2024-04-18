#!/usr/bin/python3
"""Console module of the HAirBnB module."""
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class creates a console for the HBNB."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """This method implements the quit command."""
        return True

    def do_EOF(self, line):
        """Indicates the EOF."""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """creates an instance of the base model."""
        if line == '':
            print("** class name missing **")
        elif line == "BaseModel":
            new_object = BaseModel()
            new_object.save()
            print(new_object.id)
        else:
            print("** class doesn't exist **")
    def do_show(self, line):
        """ prints the string representation of an instance based on the
        class name."""

        print(hell)



if __name__ == '__main__':
    HBNBCommand().cmdloop()

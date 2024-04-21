#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

classes = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    """This console program for the HBNB"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the console program."""
        return True
    
    def do_EOF(self, line):
        """Quits the console program"""
        return True

    def emptyline(self):
        """Emptyline does nothing"""
        pass

    def do_create(self, line):
        """Create an instance of the BaseClass Model"""
        if line == 'BaseModel':
            new_object = BaseModel()
            new_object.save()
            print(new_object.id)
        elif line == '':
            print("** class name is missing **")
        else:
            print("** class name doesn't exist **")

    def do_show(self, line):
        """Print string representation of an instance based on class name and
        id
        """
        args = line.split()
        if len(args) == 2:
            if args[0] in classes:
                if f"{args[0]}.{args[1]}" in FileStorage._FileStorage__objects:
                    print(FileStorage._FileStorage__objects\
                            [f"BaseModel.{args[1]}"])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
            print("** class name is missing **")
    
    def do_destroy(self, line):
        """Delete an instance based on classname and id and save changes"""
        args = line.split()
        if len(args) == 2:
            if args[0] in classes:
                if f"BaseModel.{args[1]}" in storage._FileStorage__objects:
                    del(storage._FileStorage__objects\
                            [f"BaseModel.{args[1]}"])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
            print("** class name is missing **")
    
    def do_all(self, line):
        """Prints all string representations based or not on class name"""
        saved_dict = storage.all().copy()
        if line == '':
            list_objs = [value.__str__() for value in saved_dict.values()]
            print(list_objs)
        elif line in classes:
            list_objs = [
                val.__str__() for val in saved_dict.values()\
                if val.__class__.__name__ == line
            ]
            print(list_objs)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, line):
        args = line.split()
        if len(args) == 4:
            if args[0] in classes:
                if f"{args[0]}.{args[1]}" in storage._FileStorage__objects:
                    saved_dict = {k: v.to_dict()\
                                  for k, v in storage.all().items()}
                    saved_dict[f"{args[0]}.{args[1]}"] = args[2]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 3:
            print("** value is missing **")
        elif len(args) == 2:
            print("** attribute name is missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 0:
            print("** class name missing **")
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

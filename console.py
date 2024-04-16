#!/usr/bin/python3
"""Console module of the HAirBnB module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class creates a console for the HBNB."""
    prompt = '(hbnb) '

    def do_quit(self):
        """This method implements the quit command."""
        return True
    def do_EOF(self):
        """This implements the EOF."""
        return True
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

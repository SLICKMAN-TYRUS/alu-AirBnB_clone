#!usr/bin/python3
"""
This file defines the console class which will
serve as the entry point of the entire project!
"""


from cmd import Cmd
from models import storage
from models.engine.errors import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Global variable of registered models
classes = storage.models


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_help(self, args):
        """
        Help command to display available commands and their descriptions.
        """
        print("Documented commands (type help <topic>):")
        print("==========================================")
        print("Quit: Quit command to exit the program")
        print("Help: Display available commands and their descriptions")
        print("")
        print("Type quit or press Ctrl-D to exit")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

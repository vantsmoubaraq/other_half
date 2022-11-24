#!/usr/bin/python3

"""
Module implements command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    class implements command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Exit the program
        """
        quit()

    def do_EOF(self, args):
        """
        Exit the program
        """
        quit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

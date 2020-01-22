#!/usr/bin/env python3
"""
Module Docstring
"""
import sys
import os.path

__author__ = "Geon George"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """

    # Check if arguement provided
    if(len(sys.argv) <= 1):
        print("Empty filename!")
        print("correct usage: python main.py image.jpg")
        return

    # Image file name (and location)
    image = sys.argv[1]

    # Check if file exist
    if(not os.path.isfile(image)):
        print("Cannot locate image: "+image)
        return

    
    print("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

#!/usr/bin/env python3
"""
Module Docstring
"""
import sys

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

    image = sys.argv[1]
    print("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

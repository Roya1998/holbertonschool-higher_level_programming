#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """
    A subclass of the built-in list class.

    Provides a method to print the list elements in ascending sorted order
    without modifying the original list.
    """

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        # The built-in sorted() function returns a new sorted list,
        # leaving the original list instance (self) unchanged.
        # This adheres to the requirement not to modify the list itself.
        print(sorted(self))
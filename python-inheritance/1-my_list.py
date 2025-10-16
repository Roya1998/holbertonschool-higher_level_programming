#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))

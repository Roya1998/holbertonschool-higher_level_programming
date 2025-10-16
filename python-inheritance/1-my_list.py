#!/usr/bin/python3
"""Defines MyList class that inherits from list."""

class MyList(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))

#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        Works for any integers in the list, including negative numbers.
        Does not modify the original list.
        """
        sorted_list = sorted(self)  # sort a copy of the list
        print(sorted_list)
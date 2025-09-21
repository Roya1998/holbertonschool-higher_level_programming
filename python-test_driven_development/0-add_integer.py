#!/usr/bin/python3
"""
Module 0-add_integer
Provides a function to add two integers.
This is part of a test-driven development project.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

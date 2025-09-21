#!/usr/bin/python3
"""
Module 0-add_integer
This module provides a function that adds two integers.
It ensures type checking and casts floats to integers before addition.
This module is part of a test-driven development project.
"""
def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: First number (must be int or float).
        b: Second number (must be int or float, defaults to 98).
    Returns:
        The integer addition of a and b.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
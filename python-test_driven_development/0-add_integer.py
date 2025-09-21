#!/usr/bin/python3
"""
This module contains a single function for adding two integers.

The function ensures that both arguments are either integers or floats,
casting floats to integers before performing the addition.
It raises a TypeError with a specific message for invalid input types.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, with a default value of 98.

    Returns:
        int: The sum of a and b.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

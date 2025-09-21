#!/usr/bin/python3
"""
0-add_integer module
This module contains a single function, `add_integer`,
that adds two numbers together. It performs type validation
and casting to ensure the operation is always on integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int: The sum of `a` and `b` as an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

"""
This module provides a function to add two integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.
    Raises:
        TypeError: If a or b are not integers or floats.
    Returns:
        int: The sum of a and b, casted to integers if they are floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
#!/usr/bin/python3
"""
7-base_geometry module
Contains the BaseGeometry class with area() and integer_validator() methods.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Public methods:
        area(self): Raises an Exception indicating it is not implemented.
        integer_validator(self, name, value): Validates if value is a positive integer.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is not implemented in the base class and raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the 'value'.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        # 1. Check if value is an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # 2. Check if value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        # If both checks pass, validation is successful.

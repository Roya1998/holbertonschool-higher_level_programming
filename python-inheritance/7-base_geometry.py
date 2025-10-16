#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Provides basic functionality, including an area method stub and
    a utility method for validating integer values.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        This method is not implemented in the base class and serves as
        a placeholder for subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and is greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        # Check if value is an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # Check if value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


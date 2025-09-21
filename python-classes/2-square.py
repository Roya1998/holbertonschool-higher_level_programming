#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Represents a square with a validated size."""

    def __init__(self, size=0):
        """Initialize the square with an optional private size attribute.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

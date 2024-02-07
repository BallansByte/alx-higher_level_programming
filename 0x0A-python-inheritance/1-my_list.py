#!/usr/bin/python3
"""Defining an inherited list class."""


class MyList(list):
    """Implementing a sorted printing for a built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

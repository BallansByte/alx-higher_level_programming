#!/usr/bin/python3
"""Defineing a class and inherited class-checer."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an instance or inherited instance.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance- True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

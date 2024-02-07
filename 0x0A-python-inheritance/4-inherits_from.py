#!/usr/bin/python3
"""Defining an inherited class-checker."""


def inherits_from(obj, a_class):
    """Checkin to know if an object is an inherited instance.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

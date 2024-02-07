#!/usr/bin/python3
"""Defines an object attr lookup function."""


def lookup(obj):
    """Returning a list of objects attributes."""
    return (dir(obj))

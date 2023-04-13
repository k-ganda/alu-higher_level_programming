#!/usr/bin/python3
"""Defibes a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>
    Args:
        first_name: The first name.
        last_name: The last name.
    Raises:
        TypeError: If first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name)

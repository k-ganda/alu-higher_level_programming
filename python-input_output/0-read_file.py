#!/usr/bin/python3
"""Defines a text file-reading funcion."""


def read_file(filename=""):
    """Print the contentes of UTF* text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

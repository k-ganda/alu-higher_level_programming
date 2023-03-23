#!/usr/bin/python3
"""Define a text-file writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The file name to write.
        text (str):The text to write to the file.
    Returns:
        The number of characters written in the text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

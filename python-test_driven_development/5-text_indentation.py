#!/usr/bin/python3
"""Defines a text identation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: A text which is a string.
    Raises:
        TypeError: If text is not a string.
    """
    for char in text:
        print(char, end="")
        if char in (".", "?", ":"):
            print("\n\n", end="")

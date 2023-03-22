#!/usr/bin/python3
"""Defines a class myInt that inherits from int."""


class myInt(int):
    """Invert int operators == and !=."""


    def __eq__(self, value):
        """Overide == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

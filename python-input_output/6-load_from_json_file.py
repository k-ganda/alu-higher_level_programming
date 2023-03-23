#!/usr/bin/python3
"""Defines a create object JSON function."""
import json


def load_from_json_file(filename):
    """Cretes an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)

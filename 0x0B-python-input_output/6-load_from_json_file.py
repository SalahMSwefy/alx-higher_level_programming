#!/usr/bin/python3
"""Load Object from a file"""
import json


def load_from_json_file(filename):
    """Load Object from a file"""
    with open(filename, mode="r") as f:
        return json.load(f)

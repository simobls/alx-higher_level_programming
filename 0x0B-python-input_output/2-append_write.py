#!/usr/bin/python3
"""
Contains the append_file function
"""


def append_write(filename="", text=""):
    """""append a text into a file(UTF8)"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

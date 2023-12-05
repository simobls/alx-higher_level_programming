#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """""write a text into a file(UTF8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

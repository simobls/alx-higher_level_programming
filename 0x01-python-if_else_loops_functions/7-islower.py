#!/usr/bin/python3
def islower(c):
    num = ord(c)
    if num in range(97, 123):
        return True
    elif num in range(65, 91):
        return False

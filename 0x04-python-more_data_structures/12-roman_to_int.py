#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    rom_keys = list(roman.keys())
    num = 0
    for ro in roman_string:
        for r_num in rom_keys:
            if ro == r_num:
                num = num + roman[r_num]
    return num

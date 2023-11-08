def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0

    for ro in roman_string[::-1]:  # Start from the end of the string
        current_value = roman[ro]
        if current_value < prev_value:
            num -= current_value
        else:
            num += current_value
        prev_value = current_value

    return num

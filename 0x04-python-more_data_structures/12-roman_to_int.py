#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
    value = 0
    prev_value = 0
    total = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for numeral in roman_string[::-1]:
        if numeral not in roman_numerals:
            return 0
        value = roman_numerals[numeral]
        prev_char = roman_string[roman_string.index(numeral) - 1]
        if roman_string.index(numeral) != 0:
            if prev_char not in roman_numerals:
                return 0
            if value // 10 > roman_numerals[prev_char]:
                return 0
        if (total > 5 and total != 10) and value == 1:
            return 0
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total

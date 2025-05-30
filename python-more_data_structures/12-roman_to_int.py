#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    x = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    chiffre = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in range(0, len(roman_string) - 1):
        if chiffre[roman_string[x]] >= chiffre[roman_string[x + 1]]:
            value += chiffre[roman_string[x]]
        else:
            value -= chiffre[roman_string[x]]
        x += 1
    value += chiffre[roman_string[x]]
    return value

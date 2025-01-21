#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    roman = 0
    if roman_string is None:
        return 0
    chiffre = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
    for roman in range(0, len(roman_string) - 1):
            if chiffre[roman_string[roman]] >= chiffre[roman_string[roman + 1]] :
                value += chiffre[roman_string[roman]]
            else:
                 value -= chiffre[roman_string[roman]]
            roman += 1
    value += chiffre[roman_string[roman]]
    return value
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    name = ""
    for key in a_dictionary:
        if max < a_dictionary[key]:
            max = a_dictionary[key]
            name = key
    return name
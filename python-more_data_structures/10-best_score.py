#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxium = 0
    name = ""
    for key in a_dictionary:
        if maxium < a_dictionary[key]:
            maxium = a_dictionary[key]
            name = key
    return name

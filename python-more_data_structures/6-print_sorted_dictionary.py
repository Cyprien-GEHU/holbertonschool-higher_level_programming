#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for new_key in sorted(a_dictionary):
        print("{:s}: {}".format(new_key, a_dictionary[new_key]))

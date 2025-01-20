#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenth = len(my_list)
    list.reverse(my_list)
    for x in range(0, lenth):
        print("{}".format(my_list[x]))

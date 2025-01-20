#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    value_max = 0
    if lenght == 0:
        return None
    for i in range(0, lenght):
        if value_max < my_list[i]:
            value_max = my_list[i]
    return(value_max)

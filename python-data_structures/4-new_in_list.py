#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenth = len(my_list)
    new = list.copy(my_list)
    if idx < 0:
        return my_list
    elif idx > lenth:
        return my_list
    else:
        new[idx] = element
        return new
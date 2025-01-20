#!/usr/bin/python3
def element_at(my_list, idx):
    lenth = len(my_list)
    if idx < 0:
        return None
    elif idx > lenth:
        return None
    else:
        return my_list[idx]

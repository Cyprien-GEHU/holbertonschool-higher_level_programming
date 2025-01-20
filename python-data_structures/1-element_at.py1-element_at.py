#!/usr/bin/python3
def element_at(my_list, idx):
    len = len(my_list)
    if idx < 0:
        return None
    elif idx > len:
        return None
    else:
        print("{}".format(my_list[idx]))
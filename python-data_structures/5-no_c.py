#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    char = ""
    lenth = len(my_string)
    for x in range(0, lenth):
        if my_string[x] == "c" or my_string[x] == "C":
            char = ""
        else:
            char = my_string[x]
        new_str = new_str + char
    return(new_str)

#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if x == "c" or x == "C":
            list.remove(x)
    return(my_string)
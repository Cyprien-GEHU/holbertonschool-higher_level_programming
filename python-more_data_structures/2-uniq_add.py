#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    data = []
    for i in my_list:
        if i not in data:
            data.append(i)
            result += int(i)
    return result
            

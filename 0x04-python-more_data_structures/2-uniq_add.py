#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for elem in my_list:
        if elem not in new_list:
            sum = sum + elem
            new_list.append(elem)
    return sum

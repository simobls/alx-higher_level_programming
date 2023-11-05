#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            result[my_list.index(i)] = True
        else:
            result[my_list.index(i)] = False
    return result

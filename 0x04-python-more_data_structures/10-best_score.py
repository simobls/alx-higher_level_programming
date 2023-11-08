#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = 0
        S = ''
        for key in a_dictionary.keys():
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                S = key
        return S

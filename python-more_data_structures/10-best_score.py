#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestKey = list(a_dictionary.keys())[0]
    bestValue = a_dictionary[bestKey]
    for key in a_dictionary:
        if a_dictionary[key] > bestValue:
            bestValue = a_dictionary[key]
            bestKey = key
    return bestKey

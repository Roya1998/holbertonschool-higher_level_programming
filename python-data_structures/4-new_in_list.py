#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    internalList = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        internalList[idx] = element
        return internalList

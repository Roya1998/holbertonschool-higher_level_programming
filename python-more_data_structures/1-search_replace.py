#!/usr/bin/python3

def search_replace(my_list, search, replace):
    myNewList = []
    for num in my_list:
        if num == search:
            myNewList.append(replace)
        else:
            myNewList.append(num)
    return myNewList

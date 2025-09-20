#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniqeNums = []
    for num in my_list:
        if num not in uniqeNums:
            sum += num
            uniqeNums.append(num)
    return sum

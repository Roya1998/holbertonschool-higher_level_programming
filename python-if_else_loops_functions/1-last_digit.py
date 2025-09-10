#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
lastNum = abs(number) % 10
if number < 0:
    lastNum = -lastNum
if lastNum > 5:
    print(string, number, "is", lastNum, "and is greater than 5")
elif lastNum == 0:
    print(string, number, "is", lastNum, "and is 0")
elif lastNum != 0 and lastNum < 6:
    if lastNum > 0:
        print(string, number, "is", lastNum, "and is less than 6 and is not 0")
    else:
        print(string, number, "is", lastNum, "and is less than 6 and not 0")
else:
    print("\n")

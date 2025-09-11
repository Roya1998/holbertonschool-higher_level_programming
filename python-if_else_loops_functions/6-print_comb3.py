#!/usr/bin/python3
for x in range(10):
    for j in range(x + 1, 10):
        if x != 8 or j != 9:
            print("{:d}{:d}".format(x, j), end=", ")
        else:
            print("{:d}{:d}".format(x, j))

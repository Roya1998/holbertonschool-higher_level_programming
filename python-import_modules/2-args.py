#!/usr/bin/python3
import sys


if (len(sys.argv) == 1):
    print(len(sys.argv), "argument")
else:
    print(len(sys.argv), "arguments")



    for x in range(len(sys.argv)): 
        print(x,":",sys.argv[x])
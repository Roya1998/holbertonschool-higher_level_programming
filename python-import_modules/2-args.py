#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if (len(sys.argv) == 1):
        print("{}: {}".format(len(sys.argv),"argument"))
    else:
        print("{}: {}".format(len(sys.argv), "arguments"))



    for x in range(len(sys.argv)): 
        print("{}: {}".format(x,sys.argv[x]))
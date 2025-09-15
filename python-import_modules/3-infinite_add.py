#!/usr/bin/python3
import sys

if __name__ == "__main__":

    def addition():
        result = 0
        for x in range(1, len(sys.argv)):
            result += int(sys.argv[x])
        print(result)

    addition()

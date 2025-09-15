#!/usr/bin/python3
import sys

if __name__ == "__main__":

  args = sys.argv[1:]
  argv_length=len(args)

  if argv_length == 0:
        print("{}:".format("0 arguments"))
  elif argv_length == 1 :
       print("{}:".format("1 argument"))          
  else:
        print("{} {}:".format(argv_length, "arguments"))



  for x in range(argv_length): 
        print("{}: {}".format(x+1, args[x]))
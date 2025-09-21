#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # print only integers
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # skip non-integers silently
            continue
    print()  # newline at the end
    return count

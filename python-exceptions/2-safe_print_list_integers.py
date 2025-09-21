#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Try to print only integers
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integers silently
            continue
        except IndexError:
            # Stop if x is bigger than list length
            break
    print()  # newline at the end
    return count

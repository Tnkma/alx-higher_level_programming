#!/usr/bin/python3

def safe_print_list(my_lists=[], x=0):
    # expected to print the list and return the count
    count = 0
    try:
        for m in range(x):
            # going through the number of x and increamenting our count
            print("{}".format(my_lists[m]), end='')
            count += 1
        print()
    except IndexError:
        print()
    return count

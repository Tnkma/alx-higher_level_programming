#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for m in range(x):
        if isinstance(my_list[m], int):
            print("{:d}".format(my_list[m]), end='')
            cont += 1
    print()
    return cont

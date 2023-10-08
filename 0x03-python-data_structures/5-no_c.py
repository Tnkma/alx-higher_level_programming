#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    for m in my_string:
        if m != 'C' and m != 'c':
            new_string += m
    return new_string

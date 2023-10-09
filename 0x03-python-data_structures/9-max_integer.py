#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_i = my_list[0]
        for m in my_list:
            if m > max_i:
                max_i = m
        return max_i

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for nums in lists:
            print("{:d}".format(nums), end=' ')
        print()

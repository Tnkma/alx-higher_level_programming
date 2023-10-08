#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for index, nums in enumerate(lists):
            print("{:d}".format(nums), end='')
            if index != len(lists) - 1:
                print(end=" ")
        print()

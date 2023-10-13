#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        s_quare = [m * m for m in i]
        new_list.append(s_quare)
    return new_list

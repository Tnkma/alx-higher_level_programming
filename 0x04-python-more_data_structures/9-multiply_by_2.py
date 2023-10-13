#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    create_dic = {}
    for i in a_dictionary:
        create_dic = a_dictionary[i] * 2
    return create_dic

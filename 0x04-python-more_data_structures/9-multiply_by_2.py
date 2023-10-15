#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    create_dic = {}
    create_dic = {key: value*2 for key, value in a_dictionary.items()}
    return create_dic

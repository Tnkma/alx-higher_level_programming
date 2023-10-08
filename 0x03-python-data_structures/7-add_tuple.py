#!/usr/bin/python3


def ensure_2(tup):

    if len(tup) < 2:
        while len(tup) < 2:
            tup += (0,)
    if len(tup) > 2:
        return tup[:2]
    return tup


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = ensure_2(tuple_a)
    tuple_b = ensure_2(tuple_b)

    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]
    return sum_1, sum_2

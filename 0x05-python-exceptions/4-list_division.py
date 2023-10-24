#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for num_1, num_2 in zip(my_list_1, my_list_2):
        result = 0
        try:
            result = num_1 / num_2
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    while len(new_list) < list_length:
        print("out of range")
        new_list.append(0)
    return new_list

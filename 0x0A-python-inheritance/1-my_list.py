#!/usr/bin/python3
"""
A function that inherits mylist from list
and prints the list in sorted ascending order.
"""
class MyList(list):
    """
    MyList inherits the class list and its properties.
    """
    def __init__(self):
        """
        Initilize the function to the class MyList
        """
        super().__init__()

    def print_sorted(self):
        """
        Return the sorted list
        """
        my_list = sorted(self)
        print(my_list)
        return my_list


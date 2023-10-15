#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_score = max(a_dictionary, key=a_dictionary.get)
        return biggest_score
    else:
        return None

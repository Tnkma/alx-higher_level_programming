#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    first_character = sentence[0]

    if sentence is None:
        first_character = None
    else:
        return length, first_character

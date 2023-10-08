#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    first_character = sentence[0]

    if not sentence:
        return None
    else:
        return length, first_character

#!/usr/bin/python3
for alphabets in range(97, 123):
    if alphabets != 101 and alphabets != 113:
        print("{:c}".format(alphabets), end='')

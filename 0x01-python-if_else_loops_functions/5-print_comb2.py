#!/usr/bin/python3
for m in range(10):
    for i in range(m+1, 10):
        if m == 8 and i == 9:
            print("{:01}{:01}".format(m, i))
        else:
            print("{:01}{:01}".format(m, i), end=', ')

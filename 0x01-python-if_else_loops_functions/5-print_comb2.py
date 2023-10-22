#!/usr/bin/python3
for m in range(100):
    if m == 99:
        print("{:02}".format(m))
    else:
        print("{:02}".format(m), end=', ')

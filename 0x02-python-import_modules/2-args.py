#!/usr/bin/python3
if __name__ == "__main__":
    import sys
de_args = len(sys.argv) - 1
if de_args == 0:
    print("{} arguments.".format(de_args))
elif de_args >= 1:

    if de_args == 1:
        print("{} argument:".format(de_args))
        for index, args in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(index, args))
    else:
        print("{} arguments:".format(de_args))
        for index, args in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(index, args))

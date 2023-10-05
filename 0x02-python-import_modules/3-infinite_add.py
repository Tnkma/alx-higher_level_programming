#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for nums in sys.argv:
        if nums != sys.argv[0]:
            sum += int(nums)
    print(sum)

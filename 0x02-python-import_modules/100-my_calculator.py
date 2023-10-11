#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators_function = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
        }
    com = len(sys.argv) - 1
    if com < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        if operator not in operators_function:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if operator == '+':
                result = add(int(sys.argv[1]), int(sys.argv[3]))
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif operator == '-':
                result = sub(int(sys.argv[1]), int(sys.argv[3]))
                print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif operator == '*':
                result = mul(int(sys.argv[1]), int(sys.argv[3]))
                print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif operator == '/':
                result = div(int(sys.argv[1]), int(sys.argv[3]))
                print("{} / {} = {}".format(ys.argv[1], sys.argv[3], result))

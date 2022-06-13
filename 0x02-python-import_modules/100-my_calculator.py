#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    import calculator_1
    add_m = 0
    sub_m = 0
    mul_m = 0
    div_m = 0
    a = len(argv)
    if (a != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    c = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        add_m = calculator_1.add(c, b)
        print("{:d} + {:d} = {:d}".format(c, b, add_m))
        exit(0)
    if argv[2] == '-':
        sub_m = calculator_1.sub(c, b)
        print("{:d} - {:d} = {:d}".format(c, b, sub_m))
        exit(0)
    if argv[2] == '*':
        mul_m = calculator_1.mul(c, b)
        print("{:d} * {:d} = {:d}".format(c, b, mul_m))
        exit(0)
    if argv[2] == '/':
        div_m = calculator_1.div(c, b)
        print("{:d} / {:d} = {:d}".format(c, b, div_m))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

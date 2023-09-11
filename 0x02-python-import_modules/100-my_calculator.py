#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.sub(a, b)
    elif op == "*":
        result = calc.mul(a, b)
    elif op == "/":
        if b == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
            result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    print(f"{a} {op} {b} = {result}")

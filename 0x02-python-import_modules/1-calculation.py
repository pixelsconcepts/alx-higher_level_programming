#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc.add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, calc.sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, calc.mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, calc.div(a, b)), end="\n")

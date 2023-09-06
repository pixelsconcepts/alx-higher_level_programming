#!/usr/bin/python3

def print_last_digit(number):
    abs_num = abs(number)
    last_digit = abs_num % 10

    print("{}".format(last_digit), end="")

    return last_digit

#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
abs_number = abs(number)
last_digit = abs_number % 10

if number < 0:
    last_digit = -last_digit

message = (f"Last digit of {number:d} is {last_digit}")

if number > 0 and last_digit > 5:
    print(message + " and is greater than 5")
elif last_digit == 0:
    print(message + " and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit}\
 and is less than 6 and not 0")

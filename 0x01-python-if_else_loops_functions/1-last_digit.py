#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
message = (f"Last digit of {number:d} is {last_digit}")
if int(last_digit) > 5:
    print(message + " and is greater than 5")
elif int(last_digit) == 0:
    print(message + " and is 0")
elif int(last_digit) < 6 and int(last_digit) == 0:
    print(message + " and is less than 6 and not 0")

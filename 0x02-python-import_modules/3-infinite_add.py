#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_sum = 0

    for arg in sys.argv[1:]:
        arg_sum += int(arg)

    print(arg_sum)


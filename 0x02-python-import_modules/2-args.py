#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{} arguments".format(len(sys.argv)-1), end="")
        print(".")
    else:
        num_args = len(sys.argv) - 1
        print("{} arguments".format(len(sys.argv)-1), end="")
        print(":")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

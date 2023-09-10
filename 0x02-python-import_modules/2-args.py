#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(f"{len(sys.argv)-1} arguments", end="")
        print(".")
    else:
        num_args = len(sys.argv) - 1

        print(f"{len(sys.argv)-1} arguments", end="")
        print(":")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Number of argument: 0.")
        print(".")
    else:
        num_args = len(sys.argv) - 1
        print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{'.' if num_args == 0 else ':'}")
        
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")


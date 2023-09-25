#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_num = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count_num += 1
    except IndexError:
        pass
    print()
    return count_num

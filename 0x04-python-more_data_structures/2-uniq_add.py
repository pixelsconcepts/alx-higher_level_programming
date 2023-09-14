#!/usr/bin/python3
def uniq_add(my_list=[]):

    add_list = 0
    uniq_nums = []

    for num in my_list:
        if num not in uniq_nums:
            uniq_nums.append(num)
            add_list += num

    return add_list

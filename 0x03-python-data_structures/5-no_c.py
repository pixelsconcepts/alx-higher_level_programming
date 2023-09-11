#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    char_list = [char for char in char_list if char.lower() != 'c']
    result = ''.join(char_list)
    return result

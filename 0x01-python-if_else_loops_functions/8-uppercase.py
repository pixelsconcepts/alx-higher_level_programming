#!/usr/bin/python3

def uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            ch_upper = ord(ch) - ord('a') + ord('A')
            result += "{}".format(chr(ch_upper))
        else:
            result += "{}".format(ch)
    result += '\n'
    print(result, end="")

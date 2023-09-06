#!/usr/bin/python3

def uppercase(s):
    for ch in s:
        if 'a' <= ch <= 'z':
            ch_upper = ord(ch) - ord('a') + ord('A')
            print("{}".format(chr(ch_upper)), end="")
        else:
            print("{}".format(ch), end="")

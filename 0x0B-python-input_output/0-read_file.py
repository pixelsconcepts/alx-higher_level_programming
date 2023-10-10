#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as file_content:
        content = file_content.read()
        print(content)
    
    return content

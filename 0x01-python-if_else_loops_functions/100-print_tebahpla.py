#!/usr/bin/python3
output = ""
for i in range(ord('z'), ord('A') - 1, -1):
    output += f"{chr(i)}"
    if i % 2 == 0:
        output += f"{chr(i - 32)}"

print(output, end="")


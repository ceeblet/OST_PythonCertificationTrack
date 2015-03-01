#!/usr/local/bin/python3
"""secret_code.py"""

input_string = "Message: "

inp = input(input_string)
new_str = ""
for c in inp:
    new_str += chr(ord(c) + 1)
print(''.join(reversed(new_str)))

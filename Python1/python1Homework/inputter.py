#!/usr/local/bin/python3
"""inputter.py"""

input_string = "Enter text: "
file_name = "user_text.txt"

old_file = open(file_name, 'a')
old_file.close()
old_file = open(file_name, 'r')
print(old_file.read())

while True:    
    s = input(input_string)
    if not s:
        break
    text_file = open(file_name, 'a')
    text_file.write(s)
    text_file = open(file_name, 'r')
    if text_file:
        print(text_file.read())

    
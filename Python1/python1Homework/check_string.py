#!/usr/local/bin/python3
"""check_string.py asks the user to input a string then verifies
   that the string is is all in upper case and ends with a period.
   If either of these tests fails, will print and appropiate message.
   If both tests succeed, will print a message that indicates the string
   is acceptable."""
   
uin = input("Please enter an upper-case string ending with a period: ")

if not uin.isupper():
    print("Input is not all upper case.")
if not uin.endswith("."):
    print("Input does not end with a period.")
elif uin.isupper() and uin.endswith("."):
    print("Input meets both requirements.")

    
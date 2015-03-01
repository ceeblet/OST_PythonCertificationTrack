#!/usr/local/bin/python3
""" divider.py """

print("Dividing 10 by an integer")
while True:
    try:
        inp = input("Provide an integer: ")
        print(10/int(inp))
    except ValueError:
        print("Your input must be an integer")
        continue
    except ZeroDivisionError:
        print("Your input must not be zero (0)")

    
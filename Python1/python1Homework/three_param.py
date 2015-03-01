#!/usr/local/bin/python3
""" three_param.py """

def my_func(a, b="b was not entered", c="c was not entered"):
    args = [a, b, c]
    for arg in args:
        print(arg)

my_func("test")
my_func("test", "Test")
my_func("test", "Test", "TEST")
print(my_func)
#!/usr/local/bin/python3
"""word_list.py"""

user_string = input("Input your text: ")
words = user_string.strip().split()
uppercase = []
noupper = []

for word in words:
    if word.istitle():
        uppercase.append(word)
    if word.islower():
        noupper.append(word)

bothlists = uppercase + noupper

for word in bothlists:
    print(word)
    
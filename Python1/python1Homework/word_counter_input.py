#!/usr/local/bin/python3
"""Count the number of different words in a text."""

text = input("Enter a line: ")

for punc in ",?;.":
    text = text.replace(punc, "")
print(text)
words = set(text.lower().split())
print("There are", len(words), "distinct words in the text.")
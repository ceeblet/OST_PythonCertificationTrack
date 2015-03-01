#!/usr/local/bin/python3
"""input_counter.py"""

myset = set()
mydict = {}
mysetlength = len(myset)
while True:
    text = input("Enter text (or Enter to quit): ")
    if not text:
        break
    for punc in ",?;.":
        text = text.replace(punc, "")
    textwords = (text.lower().split())
    for word in textwords:
        myset.add(word)
        if len(myset) > mysetlength:
            mydict[word] = len(myset)
            mysetlength = len(myset)
    for word in (mydict.keys()):
        print(word, mydict[word])  
print("Finished")
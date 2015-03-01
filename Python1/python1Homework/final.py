#!/usr/local/bin/python3
""" final.py 
    * Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
    * The program reads all the input, splitting it up into words, and computes the length of each word. Punctuation marks 
    should not be included as a part of the word, so "it's" should be counted as a three-character word, and "final." 
    should be counted as a five-character word.
    * The example text includes a "word" of zero length (the "&"); your solution should handle this.
    * When all input has been processed ,the program should print a table showing the word count for each of the word lengths 
    that has been encountered. Your tutor will run your code against several standardized inputs to verify the correctness of your logic.
"""

import sys

def process_text(text_file):
    '''Counts the number of words of the same length in text read from a file.
    
    #>>> process_text("declaration.txt")
    >>> process_text(sys.argv[1])
    {1: 16, 2: 267, 3: 267, 4: 169, 5: 140, 6: 112, 7: 99, 8: 68, 9: 61, 10: 56, 11: 35, 12: 13, 13: 9, 14: 7, 15: 2}
    
    >>> process_text("declaration.doc")
    Traceback (most recent call last):
    ...
    IOError: [Errno 2] No such file or directory: 'declaration.doc'
    '''
    
    try: 
        f = open(text_file, 'r')
    except IOError:
        #print("Document not found")
        raise
    text = f.read()
    f.close()
    for punc in ",?;.,',:,-,(,),/":
        text = text.replace(punc, "")
    words = text.split()
    freq = {}
    for word in words:
        if len(word) != 0 and word != "&":
            freq[len(word)] = freq.get(len(word), 0) + 1
    return freq
    
def myprint(mydict):
    print("Length Count")
    for k in (mydict.keys()):
        print("{0} {1}".format(k, mydict[k]))

def _test():
    import doctest, final
    return doctest.testmod(final)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("final.py takes a filename argument.")
        sys.exit()
    else:
        input_file = sys.argv[1]
    _test() 
    myprint(process_text(input_file))
    
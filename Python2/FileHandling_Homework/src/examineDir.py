'''
Created on Oct 31, 2013

@author: cbrown
'''

import os
import glob

def examineDir():
    #currentDir = os.getcwd()
    files = (glob.glob(os.path.join(os.getcwd(), "*")))
    freq = {}
    for fn in files:
        #print(fn)
        path_extension = os.path.splitext(fn)
        extension = path_extension[1].replace(".", "")
        #print(extension)
        freq[extension] = freq.get(extension, 0)+1
    for ext in sorted(freq.keys()):
        print(ext, freq[ext])
    return freq

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    examineDir()

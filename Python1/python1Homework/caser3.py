#!/usr/local/bin/python3
""" caser.py """

import sys

print("start")
#if __name__ == "__main__":
switch = {
    'capitalize':str.capitalize,
    'title':str.title,
    'upper':str.upper,
    'lower':str.lower,
    'exit': sys.exit()
}
print("after switch")
options = switch.keys()
print("after options")
while True:
    print("in the while")
    prompt1 = 'Enter a function name ({0}) '.format(', '.join(options))
    prompt2 = 'Enter a string: '
    
    inp1 = input(prompt1)
    inp2 = input(prompt2)
    
    #option = switch.get(inp1, None)
    
    if inp1:
        #printstr = option(inpstr)
        printstr = switch[inp1](inp2)
        print(option(printstr))
        print("-" * 30)
    else:
        print("Please enter a valid option!")
    
    
#!/usr/local/bin/python3
""" caser.py """

import sys

def capitalize(mystr):
    """ capitalize(str) - takes a string
    and returns the string with first letter
    capitalized.
    """
    return mystr.capitalize()
    #print(mystr.capitalize())

def title(mystr):
    """ title(str) - takes a string and
    returns the string in title form.
    """
    return mystr.title()
    #print(mystr.title())
    
def upper(mystr):
    """ upper(str) - takes a string and 
    makes it all caps.
    """
    return mystr.upper()
    #print(mystr.upper())

def lower(mystr):
    """ lower(str) - takes a string and
    makes it all lowercase.
    """
    return mystr.lower()
    #print(mystr.lower())
    
def exit(mystr):
    """ exit() - ends the program."""
    print("Goodbye for now!")
    sys.exit()
    

if __name__ == "__main__":
    switch = {
        'capitalize': capitalize,
        'title': title,
        'upper': upper,
        'lower': lower,
        'exit': exit
    }

    options = switch.keys()

    while True:
        prompt1 = 'Enter a function name ({0}) '.format(', '.join(options))
        prompt2 = 'Enter a string: '
    
        inp1 = input(prompt1)
        inp2 = input(prompt2)
    
        option = switch.get(inp1, None)
        if option:
            print(option(inp2))
            print("-" * 30)
        else:
            print("Please enter a valid option!")
    
    
"""
Find the start and end positions of the phrase "Regular Expressions" in a 
given text block.
"""

import re

def find_position(phrase, mystring):
    m = re.search(phrase, mystring)
    if m:
        return m.span()
    else:
        return None
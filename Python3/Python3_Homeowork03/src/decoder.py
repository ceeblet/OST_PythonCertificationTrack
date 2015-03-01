"""
When passed a list, simply return objects as-is unless they are integers between 1 
and 26, in which case it should convert that number to the corresponding letter. 
The integer-to-letter correspondence is 1=A, 2=B, 3=C, 4=D, and so on.
"""

#def alphabator(lst):
#    genx = (chr(x+64) for x in lst if x in range(1,27))
#    return genx

def alphabator(lst):
    for x in lst:
        if x in range(1,27):
            yield chr(x+64)
        else:
            yield x

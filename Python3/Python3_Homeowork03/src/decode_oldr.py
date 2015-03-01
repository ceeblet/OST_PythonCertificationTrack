"""
When passed a list, simply return objects as-is unless they are integers between 1 
and 26, in which case it should convert that number to the corresponding letter. 
The integer-to-letter correspondence is 1=A, 2=B, 3=C, 4=D, and so on.
"""

def alphabator(lst):
    #genex = (chr(x+64) for x in lst if x in range(1,27))
    for x in lst:
        #print(x)
        if isinstance(x, int) and x in range(1,27):
            #print("generating..")
            (chr(x+64) for x in lst if x in range(1,27))               
        else:
            #print("returning lst")
            return x

#def alphabator(lst):
#    for i in lst:
#        if i in range(1,27):
#            yield chr(i+64)
#        else:
#            yield i

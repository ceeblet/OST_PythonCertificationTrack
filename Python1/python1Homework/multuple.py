#!/usr/local/bin/python3
"""multuple.py"""

data = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for x in data:
    result = x[0]*x[1]
    print("{0:>4} = {1:>2} x {2:>2}".format(result, x[0], x[1]))
    
# instructor suggested another way to do this more elegantly   
#    for t1, t2 in tup:
#    print("{2:>4} = {0:>2} * {1:>2}".format(t1, t2, t1*t2))
    
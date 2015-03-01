#!/usr/local/bin/python3
"""Print al factorials less than 1000."""

#c = 0
c = 1
f = 1
while (f < 1000):
    print(f)
    c += 1
#    f = 1
    f *= c
#    for n in range(c, 0, -1):
#        f = f * n

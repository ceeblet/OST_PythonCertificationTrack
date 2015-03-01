#
#case_convert.py
#
s = "this Is a Simple string"
slower = s.lower()
supper = s.upper()
stitle = s.title()
scap = s.capitalize()
sislow = s.islower()
sswap = s.swapcase()
scount = s.count("s")
scontains = s.__contains__("x")
slen = s.__len__()
ssize = s.__sizeof__()
#print(s, slower, supper, stitle, scap, sislow, sswap, scount, scontains, sep="\n")
print(slen, ssize, sep="\n")
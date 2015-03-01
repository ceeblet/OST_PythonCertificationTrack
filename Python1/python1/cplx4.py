#!/usr/local/bin/python3
""" Initial implementation of complex numbers. """

class Cplx:
   
    def __init__(c, real, imag):
        c.real = real
        c.imag = imag
    
    def __add__(c1, c2):
        c = Cplx(c1.real+c2.real, c1.imag+c2.imag)
        return c
    
    def __str__(c):
        return "%s+%sj" % (c.real, c.imag)
    
if __name__ == "__main__":
    zero = Cplx(0.0, 0.0)
    one = Cplx(1.0, 0.0)
    i = Cplx(0.0, 1.0)
    result = zero + one + i
    print(result)
    
    
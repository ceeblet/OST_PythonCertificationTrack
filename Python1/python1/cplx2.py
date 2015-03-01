#!/usr/local/bin/python3
""" Initial implementation of complex numbers. """

class Cplx:
   
    def cinit(c, real, imag):
        c.real = real
        c.imag = imag
    
    def cadd(c1, c2):
        c = Cplx()
        c.real = c1.real+c2.real
        c.imag = c1.imag+c2.imag
        return c
    
    def cstr(c):
        return "%s+%sj" % (c.real, c.imag)
    
if __name__ == "__main__":
    zero = Cplx()
    zero.cinit(0.0, 0.0)
    one = Cplx()
    one.cinit(1.0, 0.0)
    i = Cplx()
    i.cinit(0.0, 1.0)
    result = zero.cadd(one.cadd(i))
    result = zero.cadd(one.cadd(i))
    print(result.cstr())
    
    
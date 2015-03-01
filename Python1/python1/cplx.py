#!/usr/local/bin/python3
""" Initial implementation of complex numbers. """

class Cplx:
    #pass
    
#def cplx(real, imag):
#    c = Cplx()
#    c.real = real
#    c.imag = imag
#    return c
    
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
    Cplx.cinit(zero, 0.0, 0.0)
    #cinit(zero, 0.0, 0.0)
    one = Cplx()
    #cinit(one, 1.0, 0.0)
    Cplx.cinit(one, 1.0, 0.0)
    i = Cplx()
    #cinit(i, 0.0, 1.0)
    Cplx.cinit(i, 0.0, 1.0)
 #   zero = cplx(0.0, 0.0)
 #   one = cplx(1.0, 0.0)
 #   i = cplx(0.0, 1.0)
    #result = cadd(zero, cadd(one, i))
    #print(cstr(result))
    result = Cplx.cadd(zero, Cplx.cadd(one, i))
    print(Cplx.cstr(result))
    
    
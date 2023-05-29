from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd


def f(x):
    return 1/x

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def trapezoidal(a,b,n, flt_digits):
    h = (b-a)/n
    sum0 = 0
    sum1 = 0

    for i in range(n+1):
        x = a+i*h
        if i == 0 or i == n:
            sum0 += f(x)
            print(i,': \t', round(rnd(x, flt_digits)[-1],10),'\t', round(rnd(f(x)/2, flt_digits)[-1],10))
        else:
            sum1 += f(x)
            print(i,': \t', round(rnd(x, flt_digits)[-1],10),'\t', round(rnd(f(x), flt_digits)[-1],10))


    sum = round(rnd(h*((sum0/2)+sum1), flt_digits)[-1],10)
    original = round(rnd(integrate.quad(f,a,b)[0], flt_digits)[-1], 7)
    RE_ = RE(original, sum)
    SD = sd(RE_)[-1]

    print("sum0: ", round(rnd(sum0, flt_digits)[-1],7))
    print("sum1: ", round(rnd(sum1, flt_digits)[-1],7))
    print("numerical sum: ", sum)
    print("original sum: ", original)
    print("RE: ", RE_)
    print("SD: ", SD)

trapezoidal(1,2,10, 8)

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


def trapezoidal(a,b,n):
    h = (b-a)/n
    sum0 = 0
    sum1 = 0

    for i in range(n+1):
        x = a+i*h
        print(i,': \t', round(x,7),'\t', round(f(x),7))
        if i == 0 or i == n:
            sum0 += f(x)
        else:
            sum1 += f(x)

    sum = round(h*((sum0/2)+sum1),7)
    original = round(integrate.quad(f,a,b)[0], 7)
    RE_ = RE(original, sum)
    SD = sd(RE_)[-1]

    print("sum0: ", round(sum0,7))
    print("sum1: ", round(sum1,7))
    print("numerical sum: ", sum)
    print("original sum: ", original)
    print("RE: ", RE_)
    print("SD: ", SD)

trapezoidal(1,2,10)

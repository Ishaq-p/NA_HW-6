from rounding import rounding as rnd
import numpy as np
from scipy import integrate


def f(x):
    return np.cbrt(x**3 + 1)

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass

def midpoint(a,b,n):
    h = (b-a)/n
    sum = 0

    for i in range(n):
        x = a + (i)*h
        if i%2!=0:
            sum += f(x)
            print(i,': \t', round(x,7),'\t', round(f(x),6))
            
    sum = round(sum * 2*h, 8)
    origianl_sum = round(integrate.quad(f,a,b)[0], 13)
    RE_ = round(RE(origianl_sum, sum), 8)

    print("numerical integrate: ", sum)
    print("original integrate: ", origianl_sum)
    print("relative error: ", RE_)

1.0713574,
midpoint(0,1,20)
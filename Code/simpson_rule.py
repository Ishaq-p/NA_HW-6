from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd


def f(x):
    return 1/(1+x**2)

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def simpson(a,b,n):
    h = (b-a)/n
    sum0 = 0
    sum1 = 0
    sum2 = 0

    for i in range(n+1):
        x = a+i*h
        if i == 0 or i == n:
            sum0 += f(x)
            print(i,': \t', round(x,7),'\t', round(f(x),8), '\t\t', round(f(x),7))
        elif i%2==0:
            sum2 += 2*f(x)
            print(i,': \t', round(x,7),'\t', round(f(x),8), '\t', round(2*f(x),7))
        else:
            sum1 += 4*f(x)
            print(i,': \t', round(x,7),'\t', round(f(x),8), '\t', round(4*f(x),7))
    
    sum = round(h/3*(sum0+(4*sum1)+(2*sum2)),8)
    # y = round(integrate.quad(f,a,b)[0], 8)
    y = 4*sum
    RE_ = RE(round(np.pi,7), y)
    SD = sd(RE_)[-1]

    # print("sum0: ", round(sum0,8))
    # print("sum1: ", round(sum1,8))
    # print("sum2: ", round(sum2,8))
    print("\nnumerical sum: ", sum)
    # print("original sum: ", y)
    print("y: ", y)
    print("pi: ", round(round(np.pi,7),7))
    print("RE: ", RE_)
    print("SD: ", SD)

simpson(0, 1, 10)
from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd



def f(x):
    return np.exp(x**2)

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def Rectangle(a,b,n):
    h = (b-a)/n
    x = a
    sum = 0
    for i in range(n):
        sum += f(x)
        print(i,': \t', round(x,7), round(f(x),7))
        x += h

    sum = round(sum * h, 8)
    origianl_sum = round(integrate.quad(f,a,b)[0], 12)
    RE_ = round(RE(origianl_sum, sum), 8)
    SD = sd(RE_)[-1]

    print("numerical integrate: ", sum)
    print("original integrate: ", origianl_sum)
    print("relative error: ", RE_)
    print("significant digits: ", SD)
    # return h*sum


Rectangle(0,0.1,10)
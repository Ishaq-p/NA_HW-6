from rounding import rounding as rnd
import numpy as np
from scipy import integrate
from sig_digits import sig_digits as sd



def f(x):
    return np.log(43.9 + (np.sin(x))**2)

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing():
    pass


def Rectangle(a,b,n, flt_digits):
    h = (b-a)/n
    x = a
    sum = 0
    for i in range(n):
        sum += f(x)
        if i in [0,5,10,15,19]:
            print(i,': \t', round(rnd(x, flt_digits)[-1], 10), round(rnd(f(x), flt_digits)[-1], 10))
        x += h

    sum = round(rnd(sum * h, flt_digits)[-1], 10)
    origianl_sum = round(rnd(integrate.quad(f,a,b)[0], flt_digits)[-1], 12)
    RE_ = round(rnd(RE(origianl_sum, sum), flt_digits)[-1], 8)
    SD = sd(RE_)[-1]

    print("numerical integrate: ", sum)
    print("original integrate: ", origianl_sum)
    print("relative error: ", RE_)
    print("significant digits: ", SD)
    # return h*sum


Rectangle(0,0.5,20, 8)
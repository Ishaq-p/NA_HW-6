from rounding import rounding as rnd
import numpy as np
# import torch


def f(x):
    return 4*x**3
    # return np.log(np.arccos(1/np.sqrt(x)))
    # pass

def RE(p1,p0):
    return abs((p1-p0)/p1)

def lagrange(x0, h):
    """
    Lagrange interpolation
    :param x: x values
    :param y: y values
    :param x0: x0 value
    :return: y0 value
    """
    x = [x0, x0+h, x0+(2*h)]
    y = [f(i) for i in x]
    n = len(x)
    L = 0
    for i in range(n):
        p = 2*x0
        for j in range(n):
            if i != j:
                p -= x[j]
        if (-1)**i<0:
            p /= (h**2)
        else:
            p /= (2*h**2)
        L += (-1)**(i) * f(x[i]) * p
    return L


def funcx(x,h):
    return (-3*f(x) + 4*f(x+h) - f(x+2*h)) / (2*h)


print(round(lagrange(1, 0.0001), 6))
print(round(funcx(1, 0.0001), 6))
print(round(funcx(2, 0.0001), 9))
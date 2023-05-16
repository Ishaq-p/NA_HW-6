from rounding import rounding as rnd
import numpy as np


def f(x):
    return x**2 - 0.17*np.sqrt(x) - 1.22

def f_(x):
    return (0.0425 / x**(3/2)) + 2

def G_b(x):
    return (b*f(x) - x*f(b)) / (f(x) - f(b))

def G_a(x):
    return (a*f(x) - x*f(a)) / (f(x) - f(a))

def RE_(x1, x0):
    return abs((x1 - x0)/x1)

def printing(n, p0, p1, RE):
    p0 = round(rnd(p0, 6)[-1], 10)
    p1 = round(rnd(p1, 6)[-1], 10)
    # RE = rnd(RE, 9)[-1]        
    print(n, ":\t||\t" ,p0,"\t||\t", p1,"\t||\t", RE)


a,b = [1,2]

def falsi_fpi(a,b, epsilon):
    n=0
    RE = 1
    alpha = f(a)*f_(a)
    print('Alpha = ', alpha)

    if alpha < 0:
        p0=a
        while RE >= epsilon:
            n+=1
            p=G_b(p0)
            RE = RE_(round(rnd(p, 6)[-1], 10), round(rnd(p0, 6)[-1], 10))
            printing(n, p0, p, RE)
            p0=p
            # use G_b

    else:
        p0=b
        while RE_(p, p0) >= epsilon:
            n+=1
            p=G_a(p0)
            RE = RE_(round(rnd(p, 6)[-1], 10), round(rnd(p0, 6)[-1], 10))
            printing(n, p0, p, RE)
            p0=p
            # use G_a

    print('Approximation of the root is', round(rnd(p, 6)[-1], 10))
falsi_fpi(1,2,1e-5)

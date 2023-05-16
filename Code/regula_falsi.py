from rounding import rounding as rnd
import numpy as np


def f(x):
    # return x - np.sin(4.221*x+2.139) + 4.221
    return x * np.sin(1/x) + 0.06044

def RE_(x1, x0):
    return abs((x1 - x0)/x1)

# def printing(n, a_n, p_n, b_n, sign, RE):
def printing(n, a_n, p_n, b_n, f_a, f_p):

    a_n = round(rnd(a_n, 6)[-1], 10)
    b_n = round(rnd(b_n, 6)[-1], 10)
    p_n = round(rnd(p_n, 6)[-1], 10)

    # if sign < 0: sign = '-'
    # else:
    #     sign = '+'
    f_a = rnd(f_a, 6)[-1]
    f_p = rnd(f_p, 6)[-1]

    # RE = rnd(RE, 9)[-1]   
          
    # print(n, ":\t||\t" ,a_n,"\t||\t", p_n,"\t||\t", b_n,"\t||\t", sign, "\t||\t", RE)
    print(n, ":\t||\t" ,a_n,"\t||\t", p_n,"\t||\t", b_n,"\t||\t", f_a, "\t||\t", f_p)

def xINT(a, b):
    return a - (f(a) * (a - b) / (f(a) - f(b)))


def regular_falsi(a, b, epsilon):
    RE=1
    n=1
    p0=a
    p=a

    # while RE >= epsilon:
    while abs(f(p)) >= epsilon:

        p = xINT(a, b)
        RE = RE_(round(rnd(p, 6)[-1], 10), round(rnd(p0, 6)[-1], 10))

        # printing(n, a, p, b, f(a)*f(p), RE)
        printing(n, a, p, b, f(a), f(p))

        Hot_Cold = f(a) * f(p)
        if Hot_Cold < 0:
            b = p
            p0 = p
        else:
            a = p
            p0 = p
        n += 1

    print('Approximation of the root is', round(rnd(p, 6)[-1], 10))

# regular_falsi( -5, -1, 1e-6)
regular_falsi( 0.06, 0.09, 1e-5)
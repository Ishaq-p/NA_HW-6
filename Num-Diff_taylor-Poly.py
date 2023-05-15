from rounding import rounding as rnd
import numpy as np
import torch
from sig_digits import sig_digits as sd


# this is the basic or initial function
def f(x):
    if type(x)==torch.Tensor:
        return torch.log(torch.arccos(1/torch.sqrt(x)))
    else:
        return np.log(np.arccos(1/np.sqrt(x)))

# this is the relative error function
def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

# this printing function prints out the the first table
def printing1(k,x,y):
    y = round(rnd(y, 7)[-1], 10)
    print(f"{k} \t||\t {x} \t||\t {y}")

# this printing function prints out the the second table
def printing2(n, z, z_, RE_, SD_):
    z = round(rnd(z.item(), 9)[-1], 15)
    z_ = round(rnd(z_, 9)[-1], 15)
    print(f"{n} \t||\t {z} \t||\t {z_} \t||\t {RE_} \t||\t {SD_}")


# this function carries out the derivative according to the taylor series
def diff_taylor(f, x, h, n):
    # f: function
    # x: point
    # h: step size
    # n: order of the derivative
    # return: nth derivative of f at x
    if n == 0:
        return f(x)
    if n == 1:
        return (f(x+h) - f(x-h)) / (2*h)
    if n == 2:
        return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)
    else:
        return (diff_taylor(f, x+h, h, n-1) - diff_taylor(f, x-h, h, n-1)) / (2*h)


# this is the main function
def main(X,h,n):

    # this is where the first table is printed
    k=[-1,0,1]
    x=[X-h,X,X+h]
    y=[f(x[0]),f(x[1]),f(x[-1])]
    for i in range(3):
        printing1(k[i],x[i],y[i])

    print() # for a new line

    # this is where we find the actual derivatives using autograd of Pytorch
    diff_=[]
    X1 = torch.tensor(float(X), requires_grad=True)
    y1 = f(X1)
    diff_.append(torch.autograd.grad(y1, X1, create_graph=True)[0])
    diff_.append(torch.autograd.grad(diff_[0], X1, create_graph=True)[0])

    # this is where the second table is printed
    for i in range(n):
        i=i+1
        f_ = diff_taylor(f, X, h, i)
        RE_ = RE(round(rnd(diff_[i-1], 9)[-1], 15), round(rnd(f_, 9)[-1], 15))
        SD_ = sd(RE_)[-1]
        printing2(f"{i} der.", diff_[i-1], f_, RE_, SD_)


if __name__ == "__main__":
    main(2, 0.01, 2)





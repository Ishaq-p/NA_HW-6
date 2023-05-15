from rounding import rounding as rnd
import numpy as np
import torch


def f(x):
    return np.log(np.arccos(1/np.sqrt(x)))

def RE(p1,p0):
    return abs(p1-p0)/abs(p0)

def printing1(k,x,y):
    y = round(rnd(y, 7)[-1], 10)
    print(f"{k} \t||\t {x} \t||\t {y}")

def printing2(n, z, z_, RE_, SD_):
    z = round(rnd(z.item(), 9)[-1], 15)
    z_ = round(rnd(z_, 9)[-1], 15)
    print(f"{n} \t||\t {z} \t||\t {z_} \t||\t {RE_} \t||\t {SD_}")

# def num_diff_taylor_poly(f, x, h, n):
#     pass

# def yup(x,h):
#     return (f(x+h) - f(x-h)) / (2*h)


def diff_taylor(f, x, h, n):
    # f: function
    # x: point
    # h: step size
    # n: order of the derivative
    # return: nth derivative of f at x
    if n == 0:
        return f(x)
    else:
        return (diff_taylor(f, x+h, h, n-1) - diff_taylor(f, x-h, h, n-1)) / (2*h)

h=0.01
X=2
n=2
k=[-1,0,1]
x=[X-h,X,X+h]
y=[f(X-h),f(X),f(X+h)]
for i in range(3):
    printing1(k[i],x[i],y[i])

print()

diff_=[]
X1 = torch.tensor(float(X), requires_grad=True)
y1 = torch.log(torch.arccos(1/torch.sqrt(X1)))
y1.backward(retain_graph=True, create_graph=True)
diff_.append(X1.grad)
y1.backward(retain_graph=True, create_graph=True)
diff_.append(X1.autograd.grad)


for i in range(n):
    i=i+1
    f_ = diff_taylor(f, X, h, i)
    printing2(f"{i} der.", diff_[i-1], f_, '*', '*')
    y1.backward()

# X1.grad.zero_()






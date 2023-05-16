from rounding import rounding as rnd
# import numpy as np


def RE(p1,p0):
    return abs((p1-p0))/abs(p1)

def printing(m, x,y,L,Y_L):
    x  =  round(rnd(x,  5 )[-1], 10)
    y  =  round(rnd(y,  5 )[-1], 10)
    L  =  round(rnd(L,  5 )[-1], 10)
    Y_L = round(rnd(Y_L, 5)[-1], 10)

    print(f"{m} \t||\t {x} \t||\t {y} \t||\t {L} \t||\t {Y_L}")

def L_(xx,x):
    n=len(x)
    L=[]

    for i in range(n):
        L.append(1)
        for j in range(n):
            if i!=j:
                L[i] *= (xx-x[j])/(x[i]-x[j])
    return L


def lagrange(x,y,xx, f_x):
    n=len(x)
    L_i=L_(xx,x)
    L=0
    m=1

    print("(n) \t\t (x)  \t\t (y) \t\t\t (L) \t\t\t  (L_i*y_i)")
    for i in range(n):
        L += L_i[i]*y[i]
        printing(m, x[i], y[i], L_i[i], L_i[i]*y[i])
        m+=1

    print(f"\nL({xx}) = {rnd(L, 5)[-1]} \nRE = {RE(f_x,L)}")


lagrange([0,43, 80, 94],[13.649, 35.606, 70.586, 84.680], 58, 50.665)





# xx=101
# x=[0,43, 80, 94]
# y=[13.649, 35.606, 70.586, 84.680]

# L0 = ((xx-x[1])*(xx-x[2])*(xx-x[3])) / ((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))
# L1 = ((xx-x[0])*(xx-x[2])*(xx-x[3])) / ((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3]))
# L2 = ((xx-x[0])*(xx-x[1])*(xx-x[3])) / ((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3]))
# L3 = ((xx-x[0])*(xx-x[1])*(xx-x[2])) / ((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2]))
# Li=[L0,L1,L2,L3]

# result=0
# for i in range(4):
#     print(Li[i]*y[i])
#     result+=Li[i]*y[i]

# print("\nL:\t",result)
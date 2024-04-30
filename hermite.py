import numpy as np
import matplotlib.pyplot as plt

x0 = -1
x1 = 0
x2 = 1
x3 = 2

f0 = 1.76103
f1 = 2
f2 = 3.76579
f3 = -7.26381
def L(i,x):
    if i == 1:
        return L1(x)
    elif i == 2:
        return L2(x)
    else:
        return L3(x)

def L1(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x-x2)*(x-x3)
    B = (x1-x2)*(x1-x3)
    return A/B


def L2(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x - x1) * (x - x3)
    B = (x2 - x1) * (x2 - x3)
    return A / B


def L3(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x - x1) * (x - x2)
    B = (x3 - x1) * (x3 - x2)
    return A / B

def dL(i,x):
    if i ==1:
        return dL1(x)
    elif i ==2:
        return dL2(x)
    else:
        return dL3(x)

def dL1(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x-x3)
    B = (x1-x2)*(x1-x3)
    C = (x-x2)
    return A/B+C/B

def dL2(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x-x1)
    B = (x2-x1)*(x2-x3)
    C = (x-x3)
    return A/B+C/B
def dL3(x):
    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x-x2)
    B = (x3-x1)*(x3-x2)
    C = (x-x1)
    return A/B+C/B

def A(i,x):


    l=[-1,0,1,2]

    return (1-2*(x-l[i])*dL(i,x))*L(i,x)**2

def B(i,x):
    l = [-1, 0, 1, 2]

    return (x-l[i])*L(i,x)**2

def P(x):
    l = [-1, 0, 1, 2]
    y = [1.76103,2,3.76579,-7.26381]
    dy = [-0.270671,1,1.53158,-42.698]

    P=0
    for i in range(1,3):
       P += A(i,x)*y[i-1] +B(i,x)*dy[i-1]
    return P

Hermite = []
field = np.linspace(-1,2,10)
for element in field:
    Hermite.append(P(element))

l = [-1, 0, 1, 2]

y = [1.76103,2,3.76579,-7.26381]

plt.plot(field,Hermite)
plt.plot(l,y)
plt.show()


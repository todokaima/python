import numpy as np
import matplotlib.pyplot as plt

def P(x):

    x0 = -1
    x1 = 0
    x2 = 1
    x3 = 2

    f0 = 1.76103
    f1 = 2
    f2 = 3.76579
    f3 = -7.26381

    A = (x-x1)*(x-x2)*(x-x3)*f0
    B = (x0-x1)*(x0-x2)*(x0-x3)
    C = (x-x0)*(x-x2)*(x-x3)*f1
    D = (x1-x0)*(x1-x2)*(x1-x3)
    E = (x-x0)*(x-x1)*(x-x3)*f2
    F = (x2-x0)*(x2-x1)*(x2-x3)
    G = (x-x0)*(x-x1)*(x-x2)*f3
    H = (x3-x0)*(x3-x2)*(x3-x2)

    return A/B+C/D+E/F+G/H

x0 = -1
x1 = 0
x2 = 1
x3 = 2

f0 = 1.76103
f1 = 2
f2 = 3.76579
f3 = -7.26381


x = np.linspace(-1,2, 15)
y = []
for element in x:
    y.append(P(element))

plt.plot(x,y)
plt.plot([x0,x1,x2,x3],[f0,f1,f2,f3])
plt.show()


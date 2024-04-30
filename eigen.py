import numpy as np

A = np.matrix('1 3 5; 2 4 6 ; 3 5 7')

x = np.matrix('1 2 5')

for i in range(3):
    A= np.dot(A,A)

print(A)

d = np.dot(A,np.transpose(x))

A = np.dot(A,A)

g = np.dot(A,np.transpose(x))

print(g[0]/d[0])
print(g[1]/d[1])
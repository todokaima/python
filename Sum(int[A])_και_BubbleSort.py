import random
length = random.randint(0,139)
A = []
A = [random.randint(1000000000000000000,100000000000000000000004444) for i in range(length)]


s = A[0]
for i in range(len(A)):
    s += A[i]
print(A)
print(s)

def Interchange(x,y):
    return y,x


def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1,0,-1):
            if a[j]<a[j-1]:
                V = a[j]
                a[j] = a[j-1]
                a[j-1] = V
    return a

print(BubbleSort(A))

C = [random.randint(100,359) for i in range(random.randint(9,90))]
Max = C[0]
for element in C:
    if element > Max:
        Max = element
print(C,"\n",Max)

def mergeSort(a, left, right, b):
    middle = (left+right)/2
    if left<middle:
        mergeSort(a,left,middle,b)
    if middle+1<right:
        mergeSort(a,middle+1,right,b)
    left = 1
    for l in range(1,middle+1):
        b[l]=a[l]

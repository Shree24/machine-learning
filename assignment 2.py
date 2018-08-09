# QUESTION 1

import numpy as np
a=np.random.rand(10,1)
print(a)
print("The mean is",a.mean())
# END

#QUESTION 2

b=np.random.rand(20,1)
print(b)
print("Variance is",b.var())
print("The standard deviation is",b.std())
#END

#QUESTION 3

A=np.random.rand(10,20)
B=np.random.rand(20,25)
print(A)
print(B)
C=A.dot(B)
print(C)
print(C.shape)
print(np.sum(C))

#QUESTION 4


def f(A):
    return(1/(1+np.exp(-A)))
A=np.arange(10).reshape(10,1)
for i in range(1,11):
    print(f(i))
# Create one-dimensional array

import numpy as np

def py_sum1(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in list(range(len(a))):
        a[i] = i **2
        b[i] = i **3
        c.append(a[i]+b[i])

    return c

def py_sum2(n):
    a = np.arange(n) **2
    b = np.arange(n) **3
    c = a+b
    return c

x = py_sum1(3)
y = py_sum2(3)
z = [i**2+i**3 for i in list(range(3))]

# print([x,list(y),z])

# Creating a multidimensional array
import numpy
m = np.array([np.arange(2),np.arange(2)])

x = np.random.randn(4,2)
print(x)
print(x.min(axis=0))


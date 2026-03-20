
import numpy as np
from numpy import random

arr = np.arange(10,31)
print(arr[-3:])


arr1 = np.linspace(1, 10, 20)
print(arr1)

arr3=np.ones(10)

print(arr3)

arr4=np.arange(1,21,2)

print(arr4)



rng=np.random.default_rng()
arr5=rng.integers(1,100,10)

print(arr5)

print(arr4.reshape(5,2))

print(np.mean(arr5))

print(np.sum(arr3))

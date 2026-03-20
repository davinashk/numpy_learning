# Importing the numpy package with the alias np
import numpy as np
from numpy import linalg

# Defining the matrix called my_matrix
first_vector = np.arange(3)
second_vector = np.array([4, 8, 15])

# YOURE CODE GOES BELOW HERE!

# Find the dot product of the vectors above
dot_product = np.dot(first_vector,second_vector)

# Find the cross product of the vectors above
cross_product = np.cross(first_vector,second_vector)

print(first_vector)
print(second_vector)

#print(np.cos(np.pi))

A = np.array([[1, 2], [2, 0]])
print(A)
print(linalg.inv(A))
print(A@linalg.inv(A))


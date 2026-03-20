# Importing the numpy package with the alias np
import numpy as np

# Defining the matrix called my_matrix
my_matrix = np.array([
                      [1, 4, 5], 
                      [10, 13, 9], 
                      [10, 8, 5]
                    ])

# YOURE CODE GOES BELOW HERE!
print(my_matrix)
# Find first column
print(my_matrix[:,[0]].shape)

# Find third row
print(my_matrix[2:])


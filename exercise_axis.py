import numpy as np

vector1 = np.zeros(0)
vector2=np.zeros(10)
#vector3=np.zeros(2,3)
vector4=np.zeros((2,3))

# Defining the matrix called my_matrix
my_matrix = np.arange(25).reshape(5,5)

# YOURE CODE GOES BELOW HERE!

# argmax of every row
argmax_row = my_matrix.max(axis=1)

#print(argmax_row)

# maximum of every row
max_row = my_matrix.argsort(axis=1)

print("my_matrix:\n",my_matrix)

every_second_row = my_matrix[::2,:]
print("every_second_row:\n",every_second_row)

# Pick out every second column of my_matrix, but in reverse order
every_second_column_reversed = my_matrix[:,::-2]
print(every_second_column_reversed)

print(my_matrix[my_matrix %2 !=0])






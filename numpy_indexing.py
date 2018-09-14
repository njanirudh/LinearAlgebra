import numpy as np

matrix = np.arange(0,12)
matrix = matrix.reshape(3,4)

print(matrix)

# only the first element
print(matrix[:1,0],"\n")

# only the first row
print(matrix[:1,:],"\n")

# only the first column
print(matrix[:,:1],"\n")

# elements in the first two rows
# and the first two columns
print(matrix[:2,:2],"\n")
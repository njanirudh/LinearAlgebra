import numpy as np

matrix_basic_1 = np.array([10,20,30])
matrix_basic_2 = np.array([15,40,90])

# Concept of vectoriztion
print(matrix_basic_1/2,"\n")
print(matrix_basic_1 - 2 , "\n")
print(matrix_basic_1 + 2 , "\n")

# Comapring two matrices
print(matrix_basic_1 < matrix_basic_2)

# Elementary operations on matrices
print(matrix_basic_1 - matrix_basic_2)
print(matrix_basic_1 + matrix_basic_2)
print(matrix_basic_1 * matrix_basic_2)
print(matrix_basic_1 / matrix_basic_2)

# Accessing and slicing array
# Similar to the python list slicing
arr = np.arange(1,11)
print(arr[-5:])
print(arr[::-1])

# Creating shallow and deep copy
# Shallow copy
shallow_arr = arr

# Deep copy
deep_arr = arr.copy()

# Changing shape of array
# Giving meaning shape
reshaped_array = arr.reshape(2,5)
print(reshaped_array)
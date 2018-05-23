import numpy as np
import sys

if __name__ == "__main__":
    # Matrix using python lists
    matrix = [0,1,2]
    matrix_2d = [[0,1,2],[1,2,3]]

    # Matrix using numpy
    np_mat = np.arange(15).reshape(3,5)
    print(np_mat)
    print(np_mat.shape)

    # Matrix with all zeros
    np_zero_mat = np.zeros((5,5),dtype=int)
    print(np_zero_mat)

    # Matrix with all ones (Identity matrix)
    # np array occupies less space compared to python list
    np_identity_mat = np.ones((5,5),dtype=int)
    print(np_identity_mat)

    # Matrix size comparison in python list vs numpy
    list_python = range(1000)
    print(sys.getsizeof(1) * len(list_python))

    np_array = np.arange(1000)
    print(np_array.size * np_array.itemsize)

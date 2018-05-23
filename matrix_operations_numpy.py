import numpy as np

if __name__ == "__main__":
    # initializing matrices
    x = np.array([[1, 2], [4, 5]])
    y = np.array([[7, 8], [9, 10]])

    # element wise addition
    print("The element wise addition of matrix is : ")
    print(np.add(x, y))

    # element wise subtraction
    print("The element wise subtraction of matrix is : ")
    print(np.subtract(x, y))

    # element wise division
    print("The element wise division of matrix is : ")
    print(np.divide(x, y))

    # element wise multiplication
    print("The element wise multiplication of matrix is : ")
    print(np.multiply(x, y))

    # matrix multiplication
    print("Matrix multiplication is : ")
    print(np.dot(x, y))

    # matrix transpose
    print("Matrix transpose is : ")
    print(np.transpose(x))

    # matrix inverse
    print("Matrix inverse is : ")
    print(np.linalg.inv(x))
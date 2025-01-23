import numpy as np

array1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

matrix1 = array1D.reshape(3,4)
print("Matrix 1: \n", matrix1)

matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix 2: \n", matrix2)

result = matrix1 + matrix2

print("\nElement-wise Addition: /n", result)

row_sums = np.sum(result, axis=1)

flattened = result.flatten()

print("\nFlattened Resulting Matrix:", flattened)
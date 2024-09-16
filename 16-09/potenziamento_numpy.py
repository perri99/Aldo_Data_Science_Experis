import numpy as np
'''
matrix = np.array([[1,2,3],
                   [4,5,6]])
matrix += 1
print(matrix.shape)
matrix1 = matrix.reshape(3,2)
print(matrix1)
'''
#Esercizio1
array = np.arange(10,50)
print(array)
print(array.dtype)
array = array.astype(float)
print(array.dtype)
print(array.shape)
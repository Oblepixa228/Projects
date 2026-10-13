import numpy as np

matrix = np.zeros((8, 8), dtype=int)

matrix[::2, ::2] = 2 
matrix[1::2, 1::2] = 2 

print(matrix)
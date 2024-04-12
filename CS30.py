import numpy as np

A = np.random.randint(0, 9, (6,2))
print(A)
rank = np.linalg.matrix_rank(A)
print("Rank of the Matrix is : ",rank)
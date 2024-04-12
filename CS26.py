import numpy as np

A = np.random.randint(0, 10, (3, 4, 3, 4))
sum = A.sum(axis=(-2, -1))
print(sum)
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)

import numpy as np

npy_mat1 = np.random.randint(10, size=(3, 3))
npy_sort = np.sort(npy_mat1)
print("Original Numpy Array : \n ", npy_mat1)
print("Sorted Numpy Array : \n ", npy_sort)

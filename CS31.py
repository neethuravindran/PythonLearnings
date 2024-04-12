import numpy as np

arr = np.array([[4, 3, 1], [5, 7, 0], [9, 9, 3], [8, 2, 4]])

print("Original array:\n", arr, "\n")

# Swapping rows 0th and 2nd
arr[[0, 2]] = arr[[2, 0]]

# Display result
print("Result:\n", arr)

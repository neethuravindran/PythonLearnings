import numpy as np

numlist = np.arange(10)
numlist[(3 < numlist) & (numlist < 9)] *= -1
print(numlist)
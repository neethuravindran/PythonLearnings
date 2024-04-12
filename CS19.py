import numpy

a = numpy.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
unique, counts = numpy.unique(a, return_counts=True)
print(dict(zip(unique, counts)))

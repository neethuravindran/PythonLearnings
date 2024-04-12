import numpy

a = numpy.array([numpy.nan, 1, 2, numpy.nan, 3, 4, 5])
print(a)
print(a[~numpy.isnan(a)])
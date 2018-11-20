import numpy

# 1D array
n = numpy.arange(27)
print(n)
print(type(n))

# two dimensional array
twon = n.reshape(3, 9)
print(twon)

# three dimensional array
threen = n.reshape(3, 3, 3)
print(threen)
print(type(threen))


import cv2
import numpy

# create numpy array out of an image
img = cv2.imread("smallgray.png", -1)
print(img)

#concatenation
print("==============================")
imh = numpy.hstack((img, img, img)) #double () is to conver the data structure to a tuple
print(imh)


imv = numpy.vstack((img, img, img)) #double () is to conver the data structure to a tuple
print(imv)

#splitting
print("==============================")
arrayhsplit = numpy.hsplit(imh, 3)
print(arrayhsplit)

arrayhsplit = numpy.vsplit(imh, 3)
print(arrayhsplit)





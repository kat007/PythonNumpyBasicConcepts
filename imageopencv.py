#pip install opencv-python
import cv2

# create numpy array out of an image
img = cv2.imread("smallgray.png", -1)
print(img)
'''
1 - cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
0 - cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
-1 - cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
'''

#write numpy array to an image
print(cv2.imwrite("newsmallgray.png", img))







import cv2

# create numpy array out of an image
img = cv2.imread("smallgray.png", -1)
print(img)


print("===================================")

#indexing
img1 = img[0:2, 2:4]
print(img1)

img2 = img[2,4]
print(img2)

print("===================================")

#slicing
for i in img:
    print(i)

for i in img.T:
    print(i)

for i in img.flat:
    print(i)
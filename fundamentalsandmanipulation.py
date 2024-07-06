import cv2
import random

## loads the image in to a numpyArray, with BGR ##

img = cv2.imread('assets/flowers.jpg', -1)

## shows that img is a numpyArray ##

print(type(img))

## prints the first line of the picture as an array ##

print(img[0])

## prints the first line, from pixel 40 to 500 ##

print(img[0][40:500])

## prints the first pixel in the first line ##

print(img[0][0])

## Takes the first 100 lines of picture and randomly gives it another value ##

""" for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
 """

## Copy and paste a part of a image ##

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
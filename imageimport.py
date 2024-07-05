import cv2

img = cv2.imread('assets/flowers.jpg', -1)
## img = cv2.resize(img, (1280, 720)) pixel argument
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) ## multiple or fraction arguments for each axis
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('New_image.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy

image= cv2.imread(r'C:\Users\Admin\Downloads\Watch this reel by totouchanemu on Instagram.jpg')
cv2.imshow('Original Image', image)

down_width= 300
down_height= 200
down_points= (down_width, down_height)
resized_down= cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
up_width= 60
up_height= 720
up_points= (up_width, up_height)
resized_up= cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)

cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up by defining height and width', resized_up)
cv2.waitKey()

cv2.destroyAllWindows()
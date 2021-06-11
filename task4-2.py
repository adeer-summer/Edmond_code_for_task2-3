#Task 4.2: Take 2 images and crop some part of both image and swap it

#import some libraries
import cv2, numpy

#read photo1
img1 = cv2.imread('/home/yasikov/Desktop/an.webp')
r_img1 = cv2.resize(img1, ( 300, 300))

cv2.imshow('photo1', r_img1)
cv2.waitKey()
cv2.destroyAllWindows()


# read Photo2
img2 = cv2.imread('/home/yasikov/Desktop/rashmika_mandanna.jpg')
r_img2 = cv2.resize(img2, ( 300, 300))

cv2.imshow('photo2', r_img2)
cv2.waitKey()
cv2.destroyAllWindows()


#crop some part ofx
crop1=r_img1[:, 0:150]
crop2 = r_img2[0:, 150: ]

#swap the both image
swap  = numpy.hstack((crop1, crop2))

#Display the swapped image
cv2.imshow('swapped_image', swap)
cv2.waitKey()
cv2.destroyAllWindows()

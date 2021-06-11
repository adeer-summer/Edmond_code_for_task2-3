#!/usr/bin/env python
# coding: utf-8


#Task 4.3: Taking 2 images differents and combinig it to form one single one image:

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


# combining two differents images to form a single one:
s2 = numpy.hstack((r_img1 , r_img2))

cv2.imshow('Joined_Photo1_and_Photo2', s2)
cv2.waitKey()
cv2.destroyAllWindows()




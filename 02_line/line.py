import numpy as np
from cv2 import cv2
from scipy import signal

#defining a few filters
vkernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
hkernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
testkernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
lpf = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
hpf = np.array([[-1/9, -1/9, -1/9], [-1/9, 8/9, -1/9], [-1/9, -1/9, -1/9]])
laplace = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

#preprocess
def preprocess(image): 
  image = cv2.imread(image) 
  image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY) 
  return image

#convolve
def conv2d(image, filter):
    img = signal.convolve2d(image, filter, boundary='symm', mode='same')
    img = np.asarray(img, np.uint8)
    return img

#main
img = preprocess('fence.jpg')
img = conv2d(img, vkernel)
img = img*40
cv2.imshow('out', img)
cv2.waitKey(0)
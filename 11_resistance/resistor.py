import cv2
import numpy as np
from scipy import signal

vkernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
lpf = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
hpf = np.array([[-1/9, -1/9, -1/9], [-1/9, 8/9, -1/9], [-1/9, -1/9, -1/9]])
s = (500, 200)

DEBUG = False
COLOUR_BOUNDS = [
                [(0, 0, 0)      , (179, 255, 93)  , "BLACK"  , 0 , (0,0,0)       ],    
                [(0, 90, 10)    , (15, 250, 100)  , "BROWN"  , 1 , (0,51,102)    ],    
                [(0, 30, 80)    , (10, 255, 200)  , "RED"    , 2 , (0,0,255)     ],
                [(10, 70, 70)   , (25, 255, 200)  , "ORANGE" , 3 , (0,128,255)   ], 
                [(30, 170, 100) , (40, 250, 255)  , "YELLOW" , 4 , (0,255,255)   ],
                [(35, 20, 110)  , (60, 45, 120)   , "GREEN"  , 5 , (0,255,0)     ],  
                [(65, 0, 85)    , (115, 30, 147)  , "BLUE"   , 6 , (255,0,0)     ],  
                [(120, 40, 100) , (140, 250, 220) , "PURPLE" , 7 , (255,0,127)   ], 
                [(0, 0, 50)     , (179, 50, 80)   , "GRAY"   , 8 , (128,128,128) ],      
                [(0, 0, 90)     , (179, 15, 250)  , "WHITE"  , 9 , (255,255,255) ],
                ];

def findResistors(liveimg):
    gliveimg = cv2.cvtColor(liveimg, cv2.COLOR_BGR2GRAY)
    resClose = []
    rectCascade = cv2.CascadeClassifier("haarcascade_resistors_0.xml")
    #detect resistors in main frame
    ressFind = rectCascade.detectMultiScale(gliveimg,1.1,25)
    for (x,y,w,h) in ressFind: #SWITCH TO H,W FOR <CV3
        
        roi_gray = gliveimg[y:y+h, x:x+w]
        roi_color = liveimg[y:y+h, x:x+w]

        #apply another detection to filter false positives
        secondPass = rectCascade.detectMultiScale(roi_gray,1.01,5)

        if (len(secondPass) != 0):
            resClose.append((np.copy(roi_color),(x,y,w,h)))
    return resClose

def process(img):
    img = signal.convolve2d(img, hpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, lpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, lpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, lpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, lpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, vkernel, boundary='symm', mode='same')
    # img = signal.convolve2d(img, hpf, boundary='symm', mode='same')
    # img = signal.convolve2d(img, hpf, boundary='symm', mode='same')
    img = np.asarray(img, np.uint8)
    return img

img = cv2.imread("down.jpg")
resclose = findResistors(img)
image = resclose[0][0]
# mask = process(image)
# print(image.shape)
# print(mask.shape)
gimage = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
gimage = cv2.resize(gimage, s)
avg = np.mean(gimage, axis = 0)
avgmask = np.zeros((s[0], len(avg)), dtype = np.uint8)
for i in range(avgmask.shape[0]):
    avgmask[i]= avg
avgmask = cv2.resize(avgmask, s)
avgmask = cv2. equalizeHist(avgmask)
cv2.imwrite("avgmask.jpg", avgmask)
avgmask = process(avgmask)

cv2.imwrite("crop.jpg", gimage)
cv2.imwrite("mask.jpg", avgmask)
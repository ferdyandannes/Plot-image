import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
cap = cv2.VideoCapture('22.mp4') #video_name is the video being called
cap.set(1,1); # Where frame_no is the frame you want
ret, frame = cap.read() # Read the frame
cv2.imwrite('window_name.jpg', frame) # show frame on window
img=mpimg.imread('window_name.jpg')
imgplot = plt.imshow(img)
plt.show()

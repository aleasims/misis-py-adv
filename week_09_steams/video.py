import cv2
import numpy as np

capture = cv2.VideoCapture('http://142.93.138.114/cars.mp4')
backSub = cv2.createBackgroundSubtractorKNN(detectShadows=True, dist2Threshold=100)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = backSub.apply(grey_frame)
    fgmask = np.stack((fgmask, fgmask, fgmask), axis=2)
    fg_img = cv2.bitwise_and(fgmask, frame)
    cv2.imshow('Foreground', fg_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

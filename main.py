# Import Libraries
import numpy as np
import cv2
import time

# using webcam
# videocapture==Read from webcam
cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0

# capture background
for i in range(50):
    ret, background = cap.read()

# capture video
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    #     convert the color space from bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Setting the values for the cloak and making masks
    # generate marks to detect red color
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])  # values is for red colour Cloth
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    # Combining the masks so that It can be viewed as in one frame
    mask1 += mask2
    # After combining the mask we are storing the value in default mask.

    # remove noise from cloth
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)
    # Combining the masks and showing them in one frame
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('Jadugar ka jaadu', final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

# so if user want to quit the program they can press Escape key the 27 is the code for escape key in

# ASCII vode values

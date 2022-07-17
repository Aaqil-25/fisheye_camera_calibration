#import libraries
import numpy as np
import cv2, time

#initialize the camera capture
#if the camera connected with FCC cable to raspberry pi.
#then, [cap =cv2.VideoCapture(0)]
#if the webcam connected with raspberry pi
#then, cap =cv2.VideoCapture(1)
cap =cv2.VideoCapture(0)

#set the camera feed frame width  height  and frame rate
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 40)

#set the all parameter to zero when initializing.
prev_frame_time = time.time()
cal_image_count = 0
frame_count = 0

while True:

     ret, frame = cap.read()
     frame_count += 1
     #when a frame count equal to 30 capture the image to avoid capturing blurry images
     if frame_count == 30:
         cv2.imwrite("cal_image_" + str(cal_image_count) + ".jpg",frame)
         cal_image_count += 1
         frame_count = 0
  
     new_frame_time = time.time()
     fps = 1/(new_frame_time - prev_frame_time)
     prev_frame_time = new_frame_time
     cv2.putText(frame, "FPS" + str(int(fps)), (10,40), cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 2, cv2.LINE_AA)
     cv2.imshow("image Feed",frame)

     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"): break

cap.release()
cv2.destroyAllWindows()

     

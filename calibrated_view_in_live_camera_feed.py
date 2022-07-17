#import libraries
import numpy as np
import cv2, time, glob
#get the calibration data from 'camera_cal.npy'
with open('camera_cal.npy', 'rb') as f:
    camera_matrix = np.load(f)
    camera_distrotion = np.load(f)
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
     new_frame_time = time.time()
     fps = 1/(new_frame_time - prev_frame_time)
     prev_frame_time = new_frame_time
     h,  w = frame.shape[:2]
     newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, camera_distrotion, (w,h), 0, (w,h))
     dst = cv2.undistort(frame, camera_matrix, camera_distrotion, None, newcameramtx)
     mapx,mapy=cv2.initUndistortRectifyMap(camera_matrix,camera_distrotion,None,newcameramtx,(w,h),5)
     dst = cv2.remap(frame,mapx,mapy,cv2.INTER_LINEAR)
     #show the distorted and undistorted camera_view
     cv2.imshow("undistorted image",dst)
     cv2.imshow("distorted image",frame)
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"): break
  
cap.release()
cv2.destroyAllWindows()

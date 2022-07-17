#import libraries
import numpy as np
import cv2, time
import glob
#set the checker boars size
#the used checerboard size 8x5
cb_width = 7
cb_heigth = 4
cb_square_size = 35.0

#set the parameter for checerboard recognition
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
cb_3D_points = np.zeros((cb_width * cb_heigth, 3), np.float32)
cb_3D_points[:,:2] = np.mgrid[0:cb_width, 0:cb_heigth].T.reshape(-1,2)*cb_square_size
list_cb_3d_points = []
list_cb_2d_img_points = []
#set the captured image location
list_images = glob.glob('*.jpg')

for frame_name in list_images:
    img = cv2.imread(frame_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (7,4),None)
    if ret ==True:
        list_cb_3d_points.append(cb_3D_points)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        list_cb_2d_img_points.append(corners2)
        cv2.drawChessboardCorners(img, (cb_width, cb_heigth), corners2, ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)
        
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(list_cb_3d_points, list_cb_2d_img_points, gray.shape[::-1],None,None)
#print the camera calibrated data: calibration matrix and distrotion
print("calibration matrix: ")
print(mtx)
print("distrotion: ",dist)

#save the calibration data to a file 'camera_cal.npy'
with open('camera_cal.npy','wb') as f:
    np.save(f, mtx)
    np.save(f,dist)

        
        


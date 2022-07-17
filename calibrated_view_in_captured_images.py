#import libraries
import numpy as np
import cv2, time, glob
#get the calibration data from 'camera_cal.npy'
with open('camera_cal.npy', 'rb') as f:
    camera_matrix = np.load(f)
    camera_distrotion = np.load(f)
#set the images location to load
list_images = glob.glob('*.jpg')

for frame_name in list_images:
    img = cv2.imread(frame_name)
    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, camera_distrotion, (w,h), 0, (w,h))
    dst = cv2.undistort(img, camera_matrix, camera_distrotion, None, newcameramtx)
    mapx,mapy=cv2.initUndistortRectifyMap(camera_matrix,camera_distrotion,None,newcameramtx,(w,h),5)
    dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

    #show the distorted and undistorted image
    cv2.imshow("undistorted image",dst)
    cv2.imshow("distorted image",img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
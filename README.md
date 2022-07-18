# fisheye_camera_calibration
The OpenCV camera calibration was done for the 5MP OV5647 fisheye camera. 

![image](https://user-images.githubusercontent.com/60856423/179384301-2477faaa-2d6c-46b4-93fa-07c702e0ea1d.png)


The calibration process was done with the OpenCV camera calibration technique.
as a first step,


1. choose the calibration checkerboard size.

in these files 8x5, 35mm size checkerboard printed on A4 size paper is used here. Then past the paper on a rigid surface to show up in front of the camera to take pictures. The 8x5, 35mm checkerboard is attached with the file.


2. Run 'calibration_image_capturing.py ' to take pictures of a checkerboard.

Run the python file and, place the checkerboard in front of the camera in a different viewpoint to capture an image. take photos for several minutes.

3. Run 'process_the_calibration_images.py' to process the taken pictures.

By running the python file calibrate the camera to find 3D points in world coordinates and their 2D locations in all images.

the calibration process is finished. also, camera calibrated data; camera matrix and distortion data are saved in a file called 'camera_cal.npy'.


to check the camera calibration run 'calibrated_view_in_captured_images.py ' and 'calibrated_view_in_live_camera_feed.py'.






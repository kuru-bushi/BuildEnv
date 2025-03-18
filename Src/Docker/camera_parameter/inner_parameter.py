#%%
import numpy as np
import cv2 as cv
import glob
import pickle
import matplotlib.pyplot as plt

# Chessboard settings. corner point number
chessboardSize = (4, 3)

# Termination criteria for corner refinement
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points (3D points in real world space)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

# Size of chessboard squares in mm
size_of_chessboard_squares_mm = 23
objp = objp * size_of_chessboard_squares_mm

# Arrays to store object points and image points
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Load chessboard images
images_pths = glob.glob('./data/indoor_45_12_snapdragon_with_gt/img/image_0_237.png')
# ./data/detail_cur1.jpg
# ../data/indoor_45_12_snapdragon_with_gt/img/image_0_253.png
img_pth = images_pths[0]

img = cv.imread(img_pth)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_small = cv.resize(img, (img.shape[1], img.shape[0]))

# Find the chessboard corners
ret, corners = cv.findChessboardCornersSB(img_small, chessboardSize, flags=0)

plt.imshow(img)
plt.show()
print(ret)

# %%
# If corners are found, refine them and store the points
if ret:
    objpoints.append(objp)
    corners2 = cv.cornerSubPix(gray, corners, chessboardSize, (-1, -1), criteria)
    imgpoints.append(corners)

    # Draw and display the corners
    cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
    plt.imshow(img)
    plt.scatter(corners[:, 0, 0], corners[:, 0, 1])

#%%
# Camera calibration
ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, img.shape[0:2], None, None)

print('-----カメラ行列-----')
print(cameraMatrix)
print('-----歪み-----')
print(dist)
print('-----回転ベクトル-----')
print(rvecs)
print('-----平行移動ベクトル-----')
print(tvecs)

# Save the calibration results for later use
print("done")
print(cameraMatrix)
plt.imshow(gray)
plt.show()

# %%
h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))

######
# undistort
dst = cv.undistort(img, cameraMatrix, dist, None, newcameramtx)
plt.imshow(dst)
plt.show()


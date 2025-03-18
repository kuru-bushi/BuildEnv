#%%
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

# read
current_dir = os.getcwd()
data_pth = os.path.join(current_dir, "../data/panda.jpg")
img = cv.imread(data_pth)
# %%
# show
img_converted = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_converted)
# cv.imshow("test",img) // docker だとエラーが出る

# %%
# edge
sobelx = cv.Sobel(img_converted, cv.CV_64F, 1, 0, ksize=5)  # x方向のSobel
sobely = cv.Sobel(img_converted, cv.CV_64F, 0, 1, ksize=5)  # y方向のSobel
# %%
plt.imshow(sobelx)
# %%
plt.imshow(sobely)
# %%
# save
cv.imwrite("./testSave.jpg", img_converted)
os.listdir(".")

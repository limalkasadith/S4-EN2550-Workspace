import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
%matplotlib inline

#Q1
t1 = np.linspace(0,50,50)
t2 = np.linspace(100,255,100)
t3 = np.linspace(150,255,106)

t = np.concatenate((t1,t2,t3),axis = 0).astype(np.uint8)
print(len(t))

img = cv.imread('emma_gray.jpg',cv.IMREAD_GRAYSCALE)
assert img is not None, "Image Not Found!!"

new_img = cv.LUT(img,t)

fig,ax = plt.subplots(1,3,figsize = [20,5])
ax[0].plot(t)
ax[1].imshow(img,cmap='gray',vmin=0,vmax=255)
ax[1].axes.xaxis.set_visible(False)
ax[1].axes.yaxis.set_visible(False)
ax[0].set_title('Intensity transformation')
ax[1].set_title('Original')
ax[2].set_title('Intensity transformed Image')
ax[2].imshow(new_img,cmap='gray',vmin=0,vmax=255)
ax[2].axes.xaxis.set_visible(False)
ax[2].axes.yaxis.set_visible(False)
plt.show()
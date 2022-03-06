#Q4
img = cv.imread('shells.png',cv.IMREAD_GRAYSCALE).astype(np.uint8)
assert img is not None, "Image Not Found!!"

eq_img = cv.equalizeHist(img)

hist_original = cv.calcHist(img,[0],None,[256],[0,256])
hist_corrected_1 = cv.calcHist(eq_img,[0],None,[256],[0,256])
# hist_corrected_2 = cv.calcHist(img_corrected_RGB_2,[0],None,[256],[0,256])

fig,ax = plt.subplots(2,2,figsize = [15,10])

ax[0][0].plot(hist_original)
ax[0][1].plot(hist_corrected_1)
ax[1][0].imshow(img,cmap = 'gray',vmin =0,vmax =255)
ax[1][1].imshow(eq_img,cmap = 'gray',vmin =0,vmax =255)

ax[0][0].set_title('Original')
ax[0][1].set_title('Equalized Image')
ax[1][0].set_title('Original')
ax[1][1].set_title('Equalized Image')

plt.show()
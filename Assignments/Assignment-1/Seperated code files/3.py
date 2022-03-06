#Q3
def gammaCorrection(img,gamma): #gamma correction only to the L plane
    temp_img = img.copy()
    invGamma = 1/gamma
    for i in range (len(img)):
        for j in range (len(img[0])):
            temp_img[i][j][0] = ((img[i][j][0] / 255) ** invGamma) * 255
    return temp_img

img = cv.imread('highlights_and_shadows.jpg').astype(np.uint8)
assert img is not None, "Image Not Found!!"

gamma_1 = 1.5
gamma_2 = 2

img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img_Lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)

img_corrected_1 = gammaCorrection(img_Lab,gamma_1)
img_corrected_2 = gammaCorrection(img_Lab,gamma_2)

img_corrected_RGB_1 = cv.cvtColor(img_corrected_1,cv.COLOR_LAB2RGB)
img_corrected_RGB_2 = cv.cvtColor(img_corrected_2,cv.COLOR_LAB2RGB)

fig,ax = plt.subplots(1,3,figsize = [20,8])

ax[0].imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
ax[0].axes.xaxis.set_visible(False)
ax[0].axes.yaxis.set_visible(False)


ax[1].imshow(img_corrected_RGB_1)
ax[1].axes.xaxis.set_visible(False)
ax[1].axes.yaxis.set_visible(False)

ax[2].imshow(img_corrected_RGB_2)
ax[2].axes.xaxis.set_visible(False)
ax[2].axes.yaxis.set_visible(False)

ax[0].set_title('Original')
ax[1].set_title('Gamma = {}'.format(gamma_1))
ax[2].set_title('Gamma = {}'.format(gamma_2))
plt.show()

hist_original = cv.calcHist(cv.cvtColor(img_RGB,cv.COLOR_BGR2RGB),[0],None,[256],[0,256])
hist_corrected_1 = cv.calcHist(img_corrected_RGB_1,[0],None,[256],[0,256])
hist_corrected_2 = cv.calcHist(img_corrected_RGB_2,[0],None,[256],[0,256])

fig,ax = plt.subplots(1,3,figsize = [20,5])

ax[0].plot(hist_original)
ax[1].plot(hist_corrected_1)
ax[2].plot(hist_corrected_2)

ax[0].set_title('Original')
ax[1].set_title('Gamma = {}'.format(gamma_1))
ax[2].set_title('Gamma = {}'.format(gamma_2))

# plt.legend(loc=1, prop={'size': 10})
plt.show()
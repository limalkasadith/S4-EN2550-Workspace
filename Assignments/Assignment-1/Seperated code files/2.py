#Q2
x = 210
t1 = np.linspace(0,0,x)
t2 = np.linspace(255,255,256-x)

y = 180
y_size = 30
t3 = np.linspace(0,0,y)
t4 = np.linspace(255,255,y_size)
t5 = np.linspace(0,0,256-y_size-y)


t_white = np.concatenate((t1,t2),axis = 0).astype(np.uint8)
t_gray = np.concatenate((t3,t4,t5),axis = 0).astype(np.uint8)
assert len(t_white)== 256, "Transformation Incorrect"
assert len(t_gray)== 256, "Transformation Incorrect"


img = cv.imread('brain_proton_density_slice.png',cv.IMREAD_GRAYSCALE).astype(np.uint8)
assert img is not None, "Image Not Found!!"

white_matter = cv.LUT(img,t_white)
gray_matter = cv.LUT(img,t_gray)
gray_matter_filtered = cv.GaussianBlur(gray_matter,(3,3),0)
# gray_matter_filtered = cv.medianBlur(gray_matter,3)


fig,ax = plt.subplots(1,2,figsize = [10,5])
ax[0].plot(t_white)
ax[1].plot(t_gray)

ax[0].set_title('White Matter')
ax[1].set_title('Gray Matter')

fig,ax = plt.subplots(1,4,figsize = [15,5])

ax[0].imshow(img,cmap='gray',vmin=0,vmax=255)
ax[0].axes.xaxis.set_visible(False)
ax[0].axes.yaxis.set_visible(False)

ax[1].imshow(white_matter,cmap='gray',vmin=0,vmax=255)
ax[1].axes.xaxis.set_visible(False)
ax[1].axes.yaxis.set_visible(False)

ax[2].imshow(gray_matter,cmap='gray',vmin=0,vmax=255)
ax[2].axes.xaxis.set_visible(False)
ax[2].axes.yaxis.set_visible(False)

ax[3].imshow(gray_matter_filtered,cmap='gray',vmin=0,vmax=255)
ax[3].axes.xaxis.set_visible(False)
ax[3].axes.yaxis.set_visible(False)

ax[0].set_title('Original')
ax[1].set_title('White Matter')
ax[2].set_title('Gray Matter')
ax[3].set_title('Gray Matter - Blured')
plt.show()
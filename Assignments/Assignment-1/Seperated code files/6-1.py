#Q6 - part A
img = cv.imread('einstein.png',cv.IMREAD_GRAYSCALE).astype('float32')
assert img is not None, "Image Not Found!!"

sobel_v = np.array([(-1,-2,-1),(0,0,0),(1,2,1)],dtype=np.float32)
sobel_h = np.array([(-1,0,1),(-2,0,2),(-1,0,1)],dtype=np.float32)

img_x = cv.filter2D(img,-1,sobel_v)
img_y = cv.filter2D(img,-1,sobel_h)

grad_mag = np.sqrt(img_x**2 +img_y**2)


fig,ax = plt.subplots(1,4,figsize=(18,6))
ax[0].imshow(img,cmap='gray',vmin=0,vmax=255)
ax[1].imshow(img_x,cmap='gray',vmin=-1020,vmax=1020)
ax[2].imshow(img_y,cmap='gray',vmin=-1020,vmax=1020)
ax[3].imshow(grad_mag,cmap='gray',vmin=0,vmax=255)

ax[0].axis('off')
ax[1].axis('off')

ax[0].set_title("Original")
ax[1].set_title("Sobel Vertical")
ax[2].set_title("Sobel Horizontal")
ax[3].set_title("$\sqrt{img_x^2 + img_y^2}$")

plt.show()
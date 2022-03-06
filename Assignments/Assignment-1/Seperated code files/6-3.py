#Q6 - part C   
img = cv.imread('einstein.png',cv.IMREAD_GRAYSCALE).astype('float32')
assert img is not None, "img Not Found!!"

sobel_h1 = np.array([[1],[2],[1]])
sobel_h2 = np.array([[1,0,-1]])

sobel_v1 = np.array([[1],[0],[-1]])
sobel_v2 = np.array([[1,2,1]])

img_y= convolve2D(img,sobel_h1)
img_yy= convolve2D(img_y , sobel_h2)

img_x= convolve2D(img,sobel_v1)
img_xx= convolve2D(img_x , sobel_v2)

grad_mag = np.sqrt(img_xx**2 + img_yy**2)

fig,ax = plt.subplots(1,4,figsize=(18,6))
ax[0].imshow(img,cmap='gray',vmin=0,vmax=255)
ax[1].imshow(img_xx,cmap='gray',vmin=-1020,vmax=1020)
ax[2].imshow(img_yy,cmap='gray',vmin=-1020,vmax=1020)
ax[3].imshow(grad_mag,cmap='gray',vmin=0,vmax=255)

ax[0].axis('off')
ax[1].axis('off')

ax[0].set_title("Original")
ax[1].set_title("Sobel Vertical")
ax[2].set_title("Sobel Horizontal")
ax[3].set_title("$\sqrt{img_x^2 + img_y^2}$")

plt.show()
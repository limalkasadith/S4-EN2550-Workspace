#Q7
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
%matplotlib inline

img = cv.imread('daisy.jpg')
assert img is not None, "Image Not Found!!"

img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

mask = np.zeros(img_RGB.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,500,500)

(mask, bgdModel, fgdModel) = cv.grabCut(img_RGB,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD),0,1).astype('uint8')
fmask = (mask == cv.GC_PR_FGD).astype("uint8") * 255
flower = img_RGB*mask2[:,:,np.newaxis]

print("a: ",cv.GC_FGD,"b: ",cv.GC_PR_FGD)
bmask = (mask == cv.GC_PR_BGD).astype("uint8") * 255
outMask = (np.where((mask == cv.GC_FGD) | (mask == cv.GC_PR_FGD), 0, 1)*255).astype(np.uint8)
background = cv.bitwise_and(img, img, mask=outMask) # Background Image

fig,ax = plt.subplots(1,4,figsize=(15,6))
ax[0].imshow(img_RGB)
ax[1].imshow(flower)
ax[2].imshow(cv.cvtColor(background,cv.COLOR_BGR2RGB))
ax[3].imshow(cv.cvtColor(fmask,cv.COLOR_BGR2RGB))

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')

ax[0].set_title("Original")
ax[1].set_title("Flower")
ax[2].set_title("Background")
ax[3].set_title("Mask")

background_blur =cv.GaussianBlur(background, (9,9), 4)
re_created = cv.add(cv.cvtColor(flower,cv.COLOR_RGB2BGR), background)
enhanced = cv.add(cv.cvtColor(flower,cv.COLOR_RGB2BGR), background_blur)

fig,ax = plt.subplots(1,4,figsize=(15,7))

ax[0].imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
ax[1].imshow(cv.cvtColor(re_created,cv.COLOR_BGR2RGB))
ax[2].imshow(cv.cvtColor(enhanced,cv.COLOR_BGR2RGB))
ax[3].imshow(cv.cvtColor(background_blur,cv.COLOR_BGR2RGB))

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')

ax[0].set_title("Original")
ax[1].set_title("Re-created Image")
ax[2].set_title("Enhanced Image")
ax[3].set_title("Gaussian Blured Background")

plt.show()
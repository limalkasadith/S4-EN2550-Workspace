#Q5 - zoom images using nearest-neighbor method
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
%matplotlib inline

def convertIndex(i,j,scale):
    x = int(i/scale)
    y = int(j/scale)
    return x,y

def zoomImg(img,scale):
    rows = int(img.shape[0]*scale)
    columns = int(img.shape[1]*scale)

    new_img = np.zeros((rows,columns,3),img.dtype)

    for i in range(rows):
        for j in range(columns):
            x,y = convertIndex(i,j,scale)
            new_img[i][j] = img[x][y]
    
    return new_img

def displayImages(image):
    img = cv.imread(image)
    assert img is not None, "Image Not Found!!"

    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    zoomed_img = zoomImg(img,2)

    fig,ax = plt.subplots(1,2,figsize =[18, 6],sharey=True,sharex=True)

    ax[0].imshow(img)
    ax[1].imshow(zoomed_img)
    ax[0].axis('off')
    ax[1].axis('off')
    ax[0].set_title('Original',loc='left')
    ax[1].set_title('Zoomed Image')

displayImages('a1q5images/im01small.png')
displayImages('a1q5images/im02small.png')
displayImages('a1q5images/im03small.png')

plt.show()
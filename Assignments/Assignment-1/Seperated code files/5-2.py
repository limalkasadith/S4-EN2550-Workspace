#Q5 - zoom images using bilinear interpolation method
def zoomImg2(img,scale):
    rows = int(img.shape[0]*scale)
    cols = int(img.shape[1]*scale)
    zoomed = cv.resize(img,(cols,rows),interpolation = cv.INTER_LINEAR) 
    return zoomed

def displayImages(image):
    img = cv.imread(image)
    assert img is not None, "Image Not Found!!"

    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    zoomed_img = zoomImg2(img,2)

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
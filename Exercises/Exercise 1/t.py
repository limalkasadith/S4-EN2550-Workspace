import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('gal_gaussian.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
f,ax = plt.subplots()
ax.imshow(img)
ax.set_title("abc")
# plt.show()
cv.imshow("abc",img)
cv.waitKey(0) 
cv.destroyAllWindows()
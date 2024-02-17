import cv2
image=cv2.imread("ace\image.jpg")
gry=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imwrite("grey.jpg",gry)
cv2.imwrite("rgb.jpg",rgb)
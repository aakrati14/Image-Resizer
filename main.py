import cv2

source = "apj abdul kalam.png"
destination ='newImage.png'
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("title" , image)

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (width , height))
cv2.imshow('newImage.png', output)
cv2.waitKey(0)

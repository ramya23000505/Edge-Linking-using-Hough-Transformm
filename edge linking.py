# In[ ]:## Read image and convert it to grayscale image
## Developed by : Ramya R
## Reg no : 212223230169
import numpy as np
import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread('bird_7.jpg', cv2.IMREAD_GRAYSCALE)
img_c = cv2.imread('bird_7.jpg', cv2.IMREAD_COLOR)
img_c = cv2.cvtColor(img_c, cv2.COLOR_BGR2RGB)
gray_rgb = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
gray = cv2.GaussianBlur(gray_img, (3, 3), 0)
plt.figure(figsize=(13, 13))
plt.subplot(1, 2, 1)
plt.imshow(img_c)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Gray Image")
plt.axis("off")
plt.show()

canny = cv2.Canny(gray, 120, 150)
plt.imshow(canny, cmap='gray')
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()

lines = cv2.HoughLinesP(canny, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=250)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_c, (x1, y1), (x2, y2), (255, 0, 0), 3)
plt.imshow(img_c)
plt.title("Result Image with Hough Transform")
plt.axis("off")
plt.show()
## Display the result

## Developed by : Ramya R
## Reg no : 212223230169



# Maximally stable extremal region extractor
# https://docs.opencv.org/3.4/d5/d51/group__features2d__main.html
# https://docs.opencv.org/3.4/d3/d28/classcv_1_1MSER.html

import cv2
import numpy as np
import imutils


# img = cv2.imread('img/AUS_P.jpg') #cv2.IMREAD_GRAYSCALE
img = cv2.imread('img/LV_ID2800.jpg')
# img = imutils.resize(img, height=600)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

vis = img.copy()
mser = cv2.MSER_create()
regions, _ = mser.detectRegions(gray)

# visualization char regions
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)

# VER!!! https://en.wikipedia.org/wiki/Maximally_stable_extremal_regions#Use_in_text_detection

# agrupar mirando los centros y haciendo crecer el raio hasta interceptar segun thresold y asi botener la linea coenctada de centro y angulo?
# como en https://docs.opencv.org/3.4/d0/d7a/classcv_1_1SimpleBlobDetector.html

# tambien se puede hacer una maskara el area y dilatarla normalmente para ver si conectan (como lo haces ahora)
# https://stackoverflow.com/questions/24385714/detect-text-region-in-image-using-opencv


# # quitar fondo y dejar solo texto
# mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
# for contour in hulls:
#     cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
# text_only = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow("text only", text_only)

cv2.waitKey(0)
cv2.destroyAllWindows()


import pytesseract
from pytesseract import Output
import cv2

# img = cv2.imread('img/LV_ID2800.jpg')
# img = cv2.imread('img/sample1_highres800.jpg')
img = cv2.imread('img/sample2_highres800.jpg')
height, width = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)
cv2.imshow('thresh', thresh)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# CHARBOX
#config https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options
#https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
# d = pytesseract.image_to_boxes(thresh, config='--psm 3 -c tessedit_char_whitelist=0123456789<ABCDEFGHIJKLMNOPQRSTUVWXYZ', output_type=Output.DICT)
# print("data", d)
# n_boxes = len(d['char'])
# for i in range(n_boxes):
#     (x1, y1, x2, y2) = (d['left'][i], d['top'][i], d['right'][i], d['bottom'][i])
#     cv2.rectangle(img, (x1, height-y1), (x2, height-y2), (0, 255, 0), 2)


# # TEXTBOX
d = pytesseract.image_to_data(thresh, config='--psm 3 -c tessedit_char_whitelist=0123456789<ABCDEFGHIJKLMNOPQRSTUVWXYZ', output_type=Output.DICT)
print("data", d)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
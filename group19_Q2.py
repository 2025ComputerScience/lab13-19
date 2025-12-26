!sudo apt update
!sudo apt install tesseract-ocr tesseract-ocr-chi-tra

!pip install pytesseract

import pytesseract
from PIL import Image
import cv2

# 開啟圖片
image = Image.open("group_name.png")
text = pytesseract.image_to_string(image, lang='chi_tra', config='--psm 10')

print("OCR 辨識結果:")
print("-" * 40)
print(text)

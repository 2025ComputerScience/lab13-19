import cv2
import numpy as np
import pytesseract

# 設定檔名
filename = 'card.png' 
# 讀取圖片
img = cv2.imread(filename)

if img is not None:
    # 影像前處理
    # 把圖片轉灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 把圖片放大2倍
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # 二值化
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thresh = cv2.bitwise_not(thresh)
    # 稍微加粗筆畫
    kernel = np.ones((2,2), np.uint8)
    thresh = cv2.erode(thresh, kernel, iterations=1)

    # 執行OCR
    raw_text = pytesseract.image_to_string(thresh, lang='chi_tra+eng', config='--psm 6')

    # 後處理修正
    fixed_text = raw_text
    fixed_text = fixed_text.replace("Christm aS", "Christmas")
    fixed_text = fixed_text.replace("Christm as", "Christmas")
    fixed_text = fixed_text.replace("ChristmaS", "Christmas")
    fixed_text = fixed_text.strip()

    # 輸出結果
    print("=" * 30)
    print("最終辨識結果：")
    print(fixed_text)
    print("=" * 30)
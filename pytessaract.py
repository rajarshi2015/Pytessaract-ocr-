# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:10:12 2021

@author: RAJ
"""
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter
import re 
img_path = 'C:/Users/RAJ/realtest/'

for i in os.listdir(img_path):
  images=Image.open(img_path+'//'+i)
  plt.imshow(images)
  plt.show()
  images_new=images.convert('LA')
  im_SHARPEN2 = images_new.filter(filter=ImageFilter.SHARPEN)
  extract = pytesseract.image_to_string(im_SHARPEN2, lang = 'eng')
  extract2 = pytesseract.image_to_string(images_new,lang = 'eng')
  final= extract+extract2  
  x = re.search(r"INCOME|TAX|Account|GOVT.", final,re.M|re.I)
  y = re.search(r"GOVERNMENT|DOB|Male|Female.", final,re.M|re.I)
if x == None and y== None:
    print('Not a pan card or adhaar card')
elif type(x)== re.Match:
    print('This is a pan card')
else:
    print('adhaar card detected')

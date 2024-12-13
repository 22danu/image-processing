# -*- coding: utf-8 -*-
"""image processing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ff62E1c2SgqDV02iBzMXheXirph3m2Et
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2

import numpy as np

import matplotlib.pyplot as plt

# %matplotlib inline
from google.colab.patches import cv2_imshow
import cv2
img = cv2.imread('/content/images.jpeg')
print(cv2_imshow(img))

img

img.shape

img3 = cv2.imread('/content/images.jpeg',0)
print(cv2_imshow(img3))

img3.shape

img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(cv2_imshow(img1))

new_image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2_imshow(new_image)

new_image.shape

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_image

img.shape

smaller_image_size=cv2.resize(img,(150,150))
cv2_imshow(smaller_image_size)
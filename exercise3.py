import numpy as np
import cv2 
from matplotlib import pyplot as plt
from skimage.data import *

imageBGR = cv2.imread('Imagens/Images/imagem2.png')
imageBGR = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB) #Migrando para RGB pois plotando com matplotlib

dst1 = cv2.blur(imageBGR,(3,3))
dst2 = cv2.blur(imageBGR,(11,11))

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

plt.subplot(121),plt.imshow(imageBGR),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst1),plt.title('Média (kernel = 3)') #dst2
plt.show()

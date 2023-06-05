#Declarando Bibliotecas
import numpy as np
import cv2
from matplotlib import pyplot as plt

#chamando imagens:
path = 'Imagens/Images/imagem23x3.png'
imgBGR = cv2.imread(path)
#Convertendo para RGB e Cinza
imgRGB = cv2.cvtColor(imgBGR,code=cv2.COLOR_BGR2RGB)

# #Histograma da Imagem BGR
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histrBGR = cv2.calcHist([imgBGR],[i],None,[256],[0,256])
#     plt.plot(histrBGR,color = col) #Histograma BGR
#     plt.xlim([0,256])
# plt.show()


img_gray = cv2.cvtColor(imgRGB,code=cv2.COLOR_RGB2GRAY)
#Histograma da Imagem Cinza
histrGRAY = cv2.calcHist([img_gray],[],None,[256],[0,256])
plt.plot(histrGRAY,color = 'k') #Histograma Imagem Cinza
plt.show()
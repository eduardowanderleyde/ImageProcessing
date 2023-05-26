import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('Imagens/Images/Flor_Joaninha.jpg')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar o algoritmo Canny para detecção de bordas
edges = cv2.Canny(gray_image, 20, 280)

# Aplicar dilatação para espessar as bordas
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel)

# Aplicar a erosão para remover ruídos
erosion_edges = cv2.erode(dilated_edges, kernel)

# Criar uma máscara em branco para os objetos segmentados
mask = np.zeros_like(image)

# Encontrar contornos dos objetos segmentados
contours, _ = cv2.findContours(erosion_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos preenchidos na máscara
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Aplicar a máscara na imagem original para preservar apenas os objetos em primeiro plano
result = cv2.bitwise_and(image, mask)

# Exibir a imagem segmentada
cv2.imshow('Imagem Segmentada', result)
cv2.waitKey(0)

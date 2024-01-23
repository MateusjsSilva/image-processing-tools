import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('img/input/quadro.png', cv2.IMREAD_COLOR)

# Definir cores em BGR
preto = [0, 0, 0]
azul = [255, 0, 0]
verde = [0, 255, 0]
amarelo = [0, 255, 255]
vermelho = [0, 0, 255]

# a. Preencher todos os buracos dos objetos pretos
mask_preto = cv2.inRange(img, preto, preto)
img[mask_preto > 0] = [255, 255, 255]

# b. Eliminar todos e somente os objetos pretos
img[mask_preto > 0] = [0, 0, 0]

# c. Preencher os buracos dos objetos de cor: azul, amarelo e verde
cores = [azul, verde, amarelo]
for cor in cores:
    mask_cor = cv2.inRange(img, cor, cor)
    img[mask_cor > 0] = [255, 255, 255]

# Salvar a imagem resultante
cv2.imwrite('resultado.png', img)
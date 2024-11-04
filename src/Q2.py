import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('img/input/lena_ruido.bmp', cv2.IMREAD_GRAYSCALE)

# Definir as 4 máscaras
mascara1 = 1/5 * np.array([[0,1,0],[1,1,1],[0,1,0]])
mascara2 = 1/9 * np.array([[1,1,1],[1,1,1],[1,1,1]])
mascara3 = 1/32 * np.array([[1,3,1],[3,16,3],[1,3,1]])
mascara4 = 1/8 * np.array([[0,1,0],[1,4,1],[0,1,0]])

mascaras = [mascara1, mascara2, mascara3, mascara4]

# Aplicar as máscaras e o filtro da mediana
imagens_filtradas = [cv2.filter2D(img,-1,mascara) for mascara in mascaras]
imagem_mediana = cv2.medianBlur(img, 3)

# Salvar as imagens filtradas em arquivos separados
for i, imagem in enumerate(imagens_filtradas):
    cv2.imwrite(f'img/output/Q2/imagem_filtrada_mask{i+1}.bmp', imagem)

cv2.imwrite(f'img/output/Q2/imagem_filtrada_mediana.bmp', imagem_mediana)

# Comparar os resultados
plt.figure(figsize=(15, 8))
plt.subplot(1,5,1),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.subplot(1,5,2),plt.imshow(imagens_filtradas[0], cmap='gray'),plt.title('Máscara 1')
plt.subplot(1,5,3),plt.imshow(imagens_filtradas[1], cmap='gray'),plt.title('Máscara 2')
plt.subplot(1,5,4),plt.imshow(imagens_filtradas[2], cmap='gray'),plt.title('Máscara 3')
plt.subplot(1,5,5),plt.imshow(imagens_filtradas[3], cmap='gray'),plt.title('Máscara 4')
plt.show()

plt.figure(figsize=(15, 8))
plt.subplot(1,2,1),plt.imshow(imagem_mediana, cmap='gray'),plt.title('Mediana')
plt.subplot(1,2,2),plt.imshow(img - imagem_mediana, cmap='gray'),plt.title('Diferença')
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lê a imagem para dilatação
img = cv2.imread("img/input/imagem.png", 0)

# Uso de abertura e fechamento para filtragem morfológica
# Realize a seguinte operação na imagem ruidosa de impressão digital
# [(((AoB)d B) e B)]
# AoB = (A e B) d B
# o = abertura, e = erosão, d = dilatação
# Aqui, a função de erosão e dilatação embutida do módulo cv2 é usada.
# Também é usada uma função embutida do cv2 para formar o elemento estruturante.

# Define o elemento estruturante como uma matriz de uns 11x11
SE = np.ones((11, 11), dtype=np.uint8)

# Função para erosão
def erosao(img, SE):
    img_erodida = cv2.erode(img, SE, 1)
    return img_erodida

# Função para dilatação
def dilatacao(img, SE):
    img_dilatada = cv2.dilate(img, SE, 1)
    return img_dilatada

# Erode a imagem
AeB = erosao(img, SE)

# Dilate a imagem erodida. Isso dá a operação de abertura
AoB = dilatacao(AeB, SE)

# Salva e imprime a imagem de abertura
cv2.imwrite("img/output/Q4/Abertura.png", AoB)
plt.figure(figsize=(5, 5))
plt.imshow(AoB, cmap="gray")
plt.title("Abertura")
plt.show()

# Dilata a imagem aberta seguida de erosão. Isso dará a operação de fechamento da imagem aberta
AoBdB = dilatacao(AoB, SE)
AoBdBeB = erosao(AoBdB, SE)

# Salva e imprime a imagem de fechamento
cv2.imwrite("img/output/Q4/Fechamento.png", AoBdBeB)
plt.figure(figsize=(5, 5))
plt.imshow(AoBdBeB, cmap="gray")
plt.title("Fechamento")
plt.show()

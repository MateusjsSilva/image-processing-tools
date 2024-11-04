import cv2
import numpy as np

def uniao(imagem1, imagem2):
    # Uniao é a operação lógica OR entre as duas imagens
    return cv2.bitwise_or(imagem1, imagem2)

def intersecao(imagem1, imagem2):
    # Intersecao é a operação lógica AND entre as duas imagens
    return cv2.bitwise_and(imagem1, imagem2)

def diferenca(imagem1, imagem2):
    # Diferença é a subtração da imagem2 da imagem1
    return cv2.subtract(imagem1, imagem2)

def redimensionar_para_mesmo_tamanho(imagem1, imagem2):
    # Redimensionar a imagem2 para ter o mesmo tamanho da imagem1
    imagem2_redimensionada = cv2.resize(imagem2, (imagem1.shape[1], imagem1.shape[0]))
    return imagem1, imagem2_redimensionada

# Carregar as imagens
#imagem1 = cv2.imread('img/input/lena_gray.bmp', cv2.IMREAD_GRAYSCALE)
#imagem2 = cv2.imread('img/input/lena_ruido.bmp', cv2.IMREAD_GRAYSCALE)

imagem1 = cv2.imread('img/input/quadrado.png', cv2.IMREAD_GRAYSCALE)
imagem2 = cv2.imread('img/input/circulo.png', cv2.IMREAD_GRAYSCALE)

# Redimensionar as imagens para terem o mesmo tamanho
imagem1, imagem2 = redimensionar_para_mesmo_tamanho(imagem1, imagem2)

# Realizar as operações morfológicas
resultado_uniao = uniao(imagem1, imagem2)
resultado_intersecao = intersecao(imagem1, imagem2)
resultado_diferenca = diferenca(imagem1, imagem2)

# Salvar os resultados
cv2.imwrite(f'img/output/Q3/imagem_uniao.png', resultado_uniao)
cv2.imwrite(f'img/output/Q3/imagem_intersecao.png', resultado_intersecao)
cv2.imwrite(f'img/output/Q3/imagem_diferenca.png', resultado_diferenca)
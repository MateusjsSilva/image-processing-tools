import cv2
import numpy as np

def dilatacao(imagem, elemento_estruturante, centro):
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, elemento_estruturante, centro)
    return cv2.dilate(imagem, elemento_estruturante)

def erosao(imagem, elemento_estruturante, centro):
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, elemento_estruturante, centro)
    return cv2.erode(imagem, elemento_estruturante)

def abertura(imagem, elemento_estruturante, centro):
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, elemento_estruturante, centro)
    return cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)

def fechamento(imagem, elemento_estruturante, centro):
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, elemento_estruturante, centro)
    return cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, elemento_estruturante)

# Carregar a imagem
imagem = cv2.imread('img/input/imagem.bmp', cv2.IMREAD_GRAYSCALE)

# Definir o elemento estruturante e o centro
elemento_estruturante = (3, 3)  # Exemplo de elemento estruturante
centro = (1, 1)  # Exemplo de centro

# Realizar as operações morfológicas
resultado_dilatacao = dilatacao(imagem, elemento_estruturante, centro)
resultado_erosao = erosao(imagem, elemento_estruturante, centro)
resultado_abertura = abertura(imagem, elemento_estruturante, centro)
resultado_fechamento = fechamento(imagem, elemento_estruturante, centro)

cv2.imwrite(f'img/output/Q4/imagem_dilatacao.bmp', resultado_dilatacao)
cv2.imwrite(f'img/output/Q4/imagem_erosao.bmp', resultado_erosao)
cv2.imwrite(f'img/output/Q4/imagem_abertura.bmp', resultado_abertura)
cv2.imwrite(f'img/output/Q4/imagem_fechamento.bmp', resultado_fechamento)
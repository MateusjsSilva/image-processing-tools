import cv2
import numpy as np

def dilatacao(imagem, elemento_estruturante, centro):
    # Aplica a dilatação na imagem
    altura, largura = imagem.shape
    resultado = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            if imagem[i, j] == 255:  # Se o pixel na imagem original é branco
                # Posiciona o elemento estruturante sobre o pixel branco e o dilata
                resultado[i - centro[0]:i - centro[0] + elemento_estruturante.shape[0],
                          j - centro[1]:j - centro[1] + elemento_estruturante.shape[1]] = np.maximum(
                    resultado[i - centro[0]:i - centro[0] + elemento_estruturante.shape[0],
                    j - centro[1]:j - centro[1] + elemento_estruturante.shape[1]],
                    elemento_estruturante)

    return resultado

def erosao(imagem, elemento_estruturante, centro):
    # Aplica a erosão na imagem
    altura, largura = imagem.shape
    resultado = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(centro[0], altura - centro[0]):
        for j in range(centro[1], largura - centro[1]):
            # Verifica se o elemento estruturante coincide com a região da imagem
            if np.array_equal(imagem[i - centro[0]:i - centro[0] + elemento_estruturante.shape[0],
                              j - centro[1]:j - centro[1] + elemento_estruturante.shape[1]], elemento_estruturante):
                # Se coincidir, define o pixel como branco
                resultado[i, j] = 255

    return resultado

def abertura(imagem, elemento_estruturante, centro):
    # Aplica a operação de abertura (erosão seguida de dilatação)
    imagem_erodida = erosao(imagem, elemento_estruturante, centro)
    resultado = dilatacao(imagem_erodida, elemento_estruturante, centro)

    return resultado

def fechamento(imagem, elemento_estruturante, centro):
    # Aplica a operação de fechamento (dilatação seguida de erosão)
    imagem_dilatada = dilatacao(imagem, elemento_estruturante, centro)
    resultado = erosao(imagem_dilatada, elemento_estruturante, centro)

    return resultado


# Carregar a imagem binária
imagem_binaria = cv2.imread('img/input/imagem.png', cv2.IMREAD_GRAYSCALE)

# Definir um elemento estruturante
# Definir um elemento estruturante (cruz 3x3)
elemento_estruturante = np.array([[0, 1, 0],
                                 [1, 1, 1],
                                       [0, 1, 0]], dtype=np.uint8)

centro_elemento_estruturante = (1, 1)

# Aplicar a dilatação
resultado_dilatacao = dilatacao(imagem_binaria, elemento_estruturante, centro_elemento_estruturante)

# Aplicar a erosão
resultado_erosao = erosao(imagem_binaria, elemento_estruturante, centro_elemento_estruturante)

# Aplicar a abertura
resultado_abertura = abertura(imagem_binaria, elemento_estruturante, centro_elemento_estruturante)

# Aplicar o fechamento
resultado_fechamento = fechamento(imagem_binaria, elemento_estruturante, centro_elemento_estruturante)

cv2.imwrite(f'img/output/Q4/imagem_dilatacao.bmp', resultado_dilatacao)
cv2.imwrite(f'img/output/Q4/imagem_erosao.bmp', resultado_erosao)
cv2.imwrite(f'img/output/Q4/imagem_abertura.bmp', resultado_abertura)
cv2.imwrite(f'img/output/Q4/imagem_fechamento.bmp', resultado_fechamento)
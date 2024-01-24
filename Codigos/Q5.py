import numpy as np
import cv2


def eliminar_objetos_pretos(imagem):
    # Esta função remove os objetos pretos da imagem

    # Convertendo a imagem para HSV para facilitar a identificação de cores
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Definindo um limite inferior e superior para a cor preta
    # Nota: isso pode precisar de ajuste dependendo da imagem
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # Criando uma máscara que identifica os pretos
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    # Invertendo a máscara para obter os não pretos
    mask_not_black = cv2.bitwise_not(mask_black)

    # Aplicando a máscara na imagem
    imagem = cv2.bitwise_and(imagem, imagem, mask=mask_not_black)

    return imagem

def preencher_buracos_objetos_coloridos(img):
    # Esta função preenche os buracos nas cores especificadas
    # Convertendo a imagem para HSV para facilitar a identificação de cores

    # Definir intervalos de cores para azul, verde e amarelo no espaço de cores HSV
    cores = {
        'azul': ([100, 150, 0], [140, 255, 255]),
        'verde': ([36, 0, 0], [86, 255, 255]),
        'amarelo': ([15, 150, 150], [35, 255, 255])
    }

    # Converter a imagem de BGR para HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for cor, (lower, upper) in cores.items():
        # Criar uma máscara para cada cor
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

        # Encontrar contornos na máscara
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Preencher os buracos em cada contorno
        for contour in contours:
            cv2.drawContours(mask, [contour], 0, (255), -1)

        # Aplicar a máscara à imagem original
        img = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    return img  # mover esta linha para fora do loop

# Carregar a imagem
imagem = cv2.imread('img/input/quadro.png')

# Preencher os buracos pretos
#imagem = preencher_buracos_objetos_pretos(imagem)

#cv2.imwrite('img/output/Q5/1.png', imagem)

# Eliminar os objetos pretos
imagem = eliminar_objetos_pretos(imagem) #ok

cv2.imwrite('img/output/Q5/eliminar_pretos.png', imagem)

imagem = preencher_buracos_objetos_coloridos(imagem)

cv2.imwrite('img/output/Q5/preencher_buracos_objetos_coloridos.png', imagem)
import cv2
import numpy as np

class ProcessadorImagem:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.img = None
        self.processed_image = None

    def carregar_imagem(self):
        self.img = cv2.imread(self.input_path, cv2.IMREAD_GRAYSCALE)

    def suavizar_imagem(self):
        self.img = cv2.GaussianBlur(self.img, (3, 3), 0)

    def aplicar_laplaciano(self):
        laplacian = cv2.Laplacian(self.img, cv2.CV_64F)
        self.processed_image = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    def aplicar_unsharp_mask(self):
        gaussian = cv2.GaussianBlur(self.img, (0, 0), 2.0)
        self.processed_image = cv2.addWeighted(self.img, 2.0, gaussian, -1.0, 0)
 
    def aplicar_highboost_filter(self, boost_factor):
        gaussian = cv2.GaussianBlur(self.img, (0, 0), 3.0)
        high_freq_detail = cv2.subtract(self.img, gaussian)
        self.processed_image = cv2.addWeighted(self.img, boost_factor, high_freq_detail, 1, 0)

    def aplicar_operador_prewitt(self):
        prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

        edges_x = cv2.filter2D(self.img, -1, prewitt_x)
        edges_y = cv2.filter2D(self.img, -1, prewitt_y)
        self.processed_image = edges_x + edges_y

    def aplicar_operador_sobel(self):
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        edges_x = cv2.filter2D(self.img, -1, sobel_x)
        edges_y = cv2.filter2D(self.img, -1, sobel_y)
        self.processed_image = edges_x + edges_y

    def salvar_resultado(self, output_filename):
        output_path = f'img/output/Q1/{output_filename}'
        cv2.imwrite(output_path, self.processed_image)

# Exemplo de uso da classe
if __name__ == "__main__":
    processador = ProcessadorImagem('img/input/lena_gray.bmp', '')

    processador.carregar_imagem()
    processador.suavizar_imagem()
    processador.aplicar_laplaciano()
    processador.salvar_resultado('lena_gray_laplacian.bmp')

    processador.carregar_imagem()
    processador.aplicar_unsharp_mask()
    processador.salvar_resultado('lena_gray_unsharp.bmp')

    processador.carregar_imagem()
    processador.aplicar_highboost_filter(boost_factor=0.5)
    processador.salvar_resultado('lena_gray_highboost.bmp')

    processador.carregar_imagem()
    processador.suavizar_imagem()
    processador.aplicar_operador_prewitt()
    processador.salvar_resultado('lena_gray_prewitt.bmp')

    processador.carregar_imagem()
    processador.suavizar_imagem()
    processador.aplicar_operador_sobel()
    processador.salvar_resultado('lena_gray_sobel.bmp')
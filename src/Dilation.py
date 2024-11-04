import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image for dilation
img2 = cv2.imread("img/input/imagem.png", 0)

# Acquire size of the image
p, q = img2.shape

# Show the image
plt.imshow(img2, cmap="gray")

# Define new image to store the pixels of dilated image
imgDilate = np.zeros((p, q), dtype=np.uint8)

# Define the structuring element
SED = np.ones((11, 11), dtype=np.uint8)
constant1 = 5  # Adjust this based on the size of the structuring element

# Dilation operation without using inbuilt CV2 function
for i in range(constant1, p - constant1):
    for j in range(constant1, q - constant1):
        temp = img2[i - constant1:i + constant1 + 1, j - constant1:j + constant1 + 1]
        product = temp * SED
        imgDilate[i, j] = np.max(product)

plt.imshow(imgDilate, cmap="gray")
cv2.imwrite("img/output/Q4/Dilatacao.png", imgDilate)

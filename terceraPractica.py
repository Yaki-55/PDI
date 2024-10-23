import cv2
import numpy as np
import matplotlib.pyplot as plt

def negativo(img):
    return 255 - img

def transformacion_gamma(img, gamma=1.5):
    invGamma = 1.0 / gamma
    return np.array(255 * (img / 255) ** invGamma, dtype='uint8')

def transformacion_logaritmica(img, c):
    s = c * np.log(1 + img)
    s = np.clip(s, 0, 255)
    return np.array(s, dtype=np.uint8)

def estiramiento_contraste(img):
    a, b = np.min(img), np.max(img)
    return 255 * (img - a) / (b - a)

def rebanada_nivel_intensidad(img, nivel, ancho=50):
    img_nueva = np.zeros(img.shape, dtype=np.uint8)
    img_nueva[(img >= nivel) & (img <= nivel + ancho)] = 255
    return img_nueva

def rebanada_plano_bit(img):
    planos_bits = []
    for bit in range(8):
        plano_bit = np.bitwise_and(img, 1 << bit) >> bit
        planos_bits.append(plano_bit * 255)
    return planos_bits

img = cv2.imread('primeraImagen.jpg', 0)

img_negativo = negativo(img)
img_gamma = transformacion_gamma(img, gamma=2.0)
img_log = transformacion_logaritmica(img, 10)
img_contraste = estiramiento_contraste(img).astype(np.uint8)
img_rebanada_intensidad = rebanada_nivel_intensidad(img, 100, 50)
img_rebanadas_bit = rebanada_plano_bit(img)

fig1, axs1 = plt.subplots(2, 3, figsize=(12, 8))

axs1[0, 0].imshow(img, cmap='gray')
axs1[0, 0].set_title('Original')

axs1[0, 1].imshow(img_negativo, cmap='gray')
axs1[0, 1].set_title('Negativo')

axs1[0, 2].imshow(img_gamma, cmap='gray')
axs1[0, 2].set_title('Transformación Gamma')

axs1[1, 0].imshow(img_log, cmap='gray')
axs1[1, 0].set_title('Transformación Logarítmica')

axs1[1, 1].imshow(img_contraste, cmap='gray')
axs1[1, 1].set_title('Estiramiento de Contraste')

axs1[1, 2].imshow(img_rebanada_intensidad, cmap='gray')
axs1[1, 2].set_title('Rebanada Nivel Intensidad')

for ax in axs1.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()


fig2, axs2 = plt.subplots(2, 4, figsize=(12, 6))

for i in range(8):
    axs2[i // 4, i % 4].imshow(img_rebanadas_bit[i], cmap='gray')
    axs2[i // 4, i % 4].set_title(f'Plano de bit {i}')

for ax in axs2.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()

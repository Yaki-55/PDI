import cv2
import numpy as np
import matplotlib.pyplot as plt

def negativo(img):
    return 255 - img

def transformacion_gamma(img, gamma=1.5):
    invGamma = 1.0 / gamma
    return np.array(255 * (img / 255) ** invGamma, dtype='uint8')

def transformacion_logaritmica(img, c, epsilon=1e-5):
    s = c * np.log(1 + img + epsilon)
    s = np.clip(s, 0, 255)
    return np.array(s, dtype=np.uint8)

def estiramiento_contraste(img):
    a, b = np.min(img), np.max(img)
    return 255 * (img - a) / (b - a)

def rebanada_nivel_intensidad(img, nivel, ancho, valor_resaltado=255, preservar_fuera=True):
    img_nueva = np.zeros_like(img)
    mascara = (img >= nivel) & (img <= (nivel + ancho))
    if preservar_fuera:
        img_nueva = np.where(mascara, valor_resaltado, img)
    else:
        img_nueva[mascara] = valor_resaltado
    return img_nueva

def rebanada_plano_bit(img):
    planos_bits = []
    for bit in range(8):
        plano_bit = np.bitwise_and(img, 1 << bit) >> bit
        planos_bits.append(plano_bit * 255)
    return planos_bits

img_list = [cv2.imread('primeraImagen.jpg', 0), 
            cv2.imread('segundaImagen.png', 0), 
            cv2.imread('cuartaImagen.png', 0)]

for i, img in enumerate(img_list):
    img_negativo = negativo(img)
    img_gamma = transformacion_gamma(img, gamma=2.0)
    img_log = transformacion_logaritmica(img, c=10)
    img_contraste = estiramiento_contraste(img)
    img_rebanada_intensidad = rebanada_nivel_intensidad(img, 100, 150)
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

    for j in range(8):
        axs2[j // 4, j % 4].imshow(img_rebanadas_bit[j], cmap='gray')
        axs2[j // 4, j % 4].set_title(f'Plano de bit {j}')

    for ax in axs2.flat:
        ax.axis('off')

    plt.tight_layout()
    plt.show()
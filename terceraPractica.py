import cv2
from pylab import *
import numpy as np

altoContraste = cv2.imread('primeraImagen.jpg',0)
bajoContraste = cv2.imread('segundaImagen.png',0)
pocaIluminacion = cv2.imread('terceraImagen.png',0)
pocaIluminacion2 = cv2.imread('cuartaImagen.png',0)

def imadjust(F, range_in=(0, 255), range_out=(0, 255), gamma=1):
    F_normalized = (F - range_in[0]) / (range_in[1] - range_in[0])
    G = (F_normalized ** gamma) * (range_out[1] - range_out[0]) + range_out[0]
    G = np.clip(G, range_out[0], range_out[1])
    return G


def devolverRango(F, range_out=(0, 255)):
    G = np.interp(F, (F.min(), F.max()), range_out)
    return G.astype(np.uint8)

if bajoContraste is None:
    print("Error: No se pudo cargar la imagen.")
else:
    negativo = imadjust(bajoContraste, (0, 1), (1, 0))
    negativo = devolverRango(negativo)
    print(negativo)
    cv2.imwrite('salida.jpg', negativo)
    cv2.imwrite('entrada.png', bajoContraste)
    cv2.imshow('img', negativo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
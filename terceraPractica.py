import cv2
from pylab import *

altoContraste = cv2.imread('primeraImagen.jpg',0)
bajoContraste = cv2.imread('segundaImagen.png',0)
pocaIluminacion = cv2.imread('terceraImagen.png',0)
pocaIluminacion2 = cv2.imread('cuartaImagen.png',0)

def imadjust(F,range_in=(0,1),range_out=(0,1),gamma=1):
    G = (((F - range_in[0]) / (range_in[1] - range_in[0])) ** gamma) * (range_out[1] - range_out[0]) + range_out[0]
    return G
def devolverRango(F, range_out=(0,255)):
    G = (F-range_out[0]/range_out[1]-range_out[0])
    return G

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
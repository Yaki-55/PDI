import cv2
import numpy as np
import matplotlib.pyplot as plt
import PyQt5

imgAltoContraste = cv2.imread("./imagenesPractica4/altoContraste.png", 0)
histAltoContraste = cv2.calcHist([imgAltoContraste], [0], None, [256], [0, 256])

imgBajoContraste = cv2.imread("./imagenesPractica4/bajoContraste.png", 0)
histBajoContraste = cv2.calcHist([imgBajoContraste], [0], None, [256], [0, 256])

imgAltaIluminacion = cv2.imread("./imagenesPractica4/altaIluminacion.png", 0)
histAltaIluminacion = cv2.calcHist([imgAltaIluminacion], [0], None, [256], [0, 256])

imgBajaIluminacion = cv2.imread("./imagenesPractica4/bajoContraste.png", 0)
histBajoContraste = cv2.calcHist([imgBajoContraste], [0], None, [256], [0, 256])

plt.plot(histAltoContraste, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
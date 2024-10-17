import cv2

altoContraste = cv2.imread('primeraImagen.jng')
bajoContraste = cv2.imread('segundaImagen.png')
pocaIluminacion = cv2.imread('terceraImagen.png')



cv2.imshow('img', entrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('salida.png', entrada)
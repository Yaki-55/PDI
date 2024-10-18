import cv2

altoContraste = cv2.imread('primeraImagen.jng')
bajoContraste = cv2.imread('segundaImagen.png')
pocaIluminacion = cv2.imread('terceraImagen.png')
pocaIluminacion2 = cv2.imread('cuartaImagen',0)

def imadjust(F,range_in=(0,1),range_out=(0,1),gamma=1):
    G = (((F - range_in[0]) / (range_in[1] - range_in[0])) ** gamma) * (range_out[1] - range_out[0]) + range_out[0]
    return G


negativo = imadjust(altoContraste, (0,1), (1,0))
_, ((ax0, ax1)) = subplots(2, 2, figsize=(10, 10))

ax1.imshow(negativo, cmap="gray")
ax1.set_title("negativo")
ax1.set_axis_off()


cv2.imshow('img', entrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('salida.png', entrada)
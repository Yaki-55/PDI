import cv2

entrada = cv2.imread('img.png',0)

print(type(entrada))
print(entrada)

cv2.imshow('img', entrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('salida.png', entrada)
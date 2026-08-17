# AULA 02 — SLIDE 13 — Canny Edge Detection
# Coloque "objetos.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
imagem = cv2.imread("objetos.jpg")
if imagem is None:
    raise FileNotFoundError('Coloque "objetos.jpg" na mesma pasta do código.')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
bordas = cv2.Canny(
    cinza,
    100,
    200
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
plt.imshow(bordas, cmap="gray")
plt.title("Bordas detectadas com Canny")
plt.axis("off")
plt.show()

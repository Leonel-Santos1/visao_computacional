# AULA 02 — SLIDE 10 — Limiarização: separando valores em grupos
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
_, binaria = cv2.threshold(
    cinza,
    127,
    255,
    cv2.THRESH_BINARY
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
plt.imshow(binaria, cmap="gray")
plt.title("Imagem binária — limiar 127")
plt.axis("off")
plt.show()

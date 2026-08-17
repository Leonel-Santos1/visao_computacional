# AULA 02 — SLIDE 06 — Conversão para tons de cinza
# Coloque "objetos.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
imagem = cv2.imread("objetos.jpg")
if imagem is None:
    raise FileNotFoundError('Coloque "objetos.jpg" na mesma pasta do código.')

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
cinza = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2GRAY
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
plt.imshow(cinza, cmap="gray")
plt.title("Imagem em tons de cinza")
plt.axis("off")
plt.show()

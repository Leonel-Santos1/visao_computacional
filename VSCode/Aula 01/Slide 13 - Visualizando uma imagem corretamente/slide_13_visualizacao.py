# AULA 01 — SLIDE 13 — Visualizando uma imagem corretamente
# Coloque "imagem.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
imagem = cv2.imread("imagem.jpg")
imagem_rgb = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2RGB
)

plt.imshow(imagem_rgb)
plt.axis("off")
plt.show()

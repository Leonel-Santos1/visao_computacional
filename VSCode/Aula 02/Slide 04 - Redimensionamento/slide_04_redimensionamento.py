# AULA 02 — SLIDE 04 — Redimensionamento
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
imagem_menor = cv2.resize(
    imagem,
    (640, 480)
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
plt.imshow(cv2.cvtColor(imagem_menor, cv2.COLOR_BGR2RGB))
plt.title("Imagem redimensionada — 640 x 480")
plt.axis("off")
plt.show()

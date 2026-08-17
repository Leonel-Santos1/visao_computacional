# AULA 02 — SLIDE 18 — Prática de morfologia: código com OpenCV
# Coloque "binaria.png" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# CÓDIGO DO SLIDE — 1. Criar os kernels
# ------------------------------------------------------------
img = cv2.imread(
    "binaria.png",
    cv2.IMREAD_GRAYSCALE
)
ret = cv2.getStructuringElement(
    cv2.MORPH_RECT, (3, 3))
cruz = cv2.getStructuringElement(
    cv2.MORPH_CROSS, (3, 3))
elipse = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE, (5, 5))

# ------------------------------------------------------------
# CÓDIGO DO SLIDE — 2. Aplicar as operações
# ------------------------------------------------------------
erosao = cv2.erode(
    img, ret, iterations=1)
dilatacao = cv2.dilate(
    img, ret, iterations=1)
abertura = cv2.morphologyEx(
    img, cv2.MORPH_OPEN, cruz)
fechamento = cv2.morphologyEx(
    img, cv2.MORPH_CLOSE, elipse)
gradiente = cv2.morphologyEx(
    img, cv2.MORPH_GRADIENT, ret)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# Permite comparar as operações pedidas no experimento do slide.
# ------------------------------------------------------------
imagens = [img, erosao, dilatacao, abertura, fechamento, gradiente]
titulos = ["Original", "Erosão", "Dilatação", "Abertura", "Fechamento", "Gradiente"]

fig, eixos = plt.subplots(2, 3, figsize=(11, 7))
for eixo, imagem_plot, titulo in zip(eixos.ravel(), imagens, titulos):
    eixo.imshow(imagem_plot, cmap="gray")
    eixo.set_title(titulo)
    eixo.axis("off")
plt.tight_layout()
plt.show()

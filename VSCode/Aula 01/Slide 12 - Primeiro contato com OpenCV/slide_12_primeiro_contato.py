# AULA 01 — SLIDE 12 — Primeiro contato com OpenCV
# Coloque "imagem.jpg" nesta pasta antes de executar.

import cv2

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
imagem = cv2.imread("imagem.jpg")

print(type(imagem))
print(imagem.shape)

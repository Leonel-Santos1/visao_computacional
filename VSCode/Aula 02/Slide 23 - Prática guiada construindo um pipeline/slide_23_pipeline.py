# AULA 02 — SLIDE 23 — Prática guiada: construindo um pipeline
# Coloque "objetos.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
img = cv2.imread("objetos.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# O próprio slide pede: "Exibir e comparar cada etapa".
# ------------------------------------------------------------
fig, eixos = plt.subplots(1, 4, figsize=(16, 4))
eixos[0].imshow(img_rgb)
eixos[0].set_title("Original")
eixos[1].imshow(gray, cmap="gray")
eixos[1].set_title("Tons de cinza")
eixos[2].imshow(blur, cmap="gray")
eixos[2].set_title("Gaussian Blur")
eixos[3].imshow(edges, cmap="gray")
eixos[3].set_title("Canny")

for eixo in eixos:
    eixo.axis("off")

plt.tight_layout()
plt.show()

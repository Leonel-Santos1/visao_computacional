# AULA 02 — SLIDE 09 — Suavização e redução de ruído
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
suave = cv2.GaussianBlur(
    imagem,
    (5, 5),
    0
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# Comparação "Antes" e "Depois", como indicado no slide.
# ------------------------------------------------------------
fig, eixos = plt.subplots(1, 2, figsize=(10, 4))
eixos[0].imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
eixos[0].set_title("Antes")
eixos[0].axis("off")
eixos[1].imshow(cv2.cvtColor(suave, cv2.COLOR_BGR2RGB))
eixos[1].set_title("Depois — Gaussian Blur")
eixos[1].axis("off")
plt.tight_layout()
plt.show()

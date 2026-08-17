# AULA 02 — SLIDE 20 — Criando uma bounding box com OpenCV
# Coloque "objetos.jpg" e "binaria.png" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
imagem = cv2.imread("objetos.jpg")
binaria = cv2.imread("binaria.png", cv2.IMREAD_GRAYSCALE)
if imagem is None or binaria is None:
    raise FileNotFoundError('Coloque "objetos.jpg" e "binaria.png" na mesma pasta.')
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if not contornos:
    raise RuntimeError("Nenhum contorno foi encontrado na imagem binária.")
contorno = contornos[0]

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
x, y, w, h = cv2.boundingRect(contorno)

cv2.rectangle(
    imagem,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title("Bounding box criada com OpenCV")
plt.axis("off")
plt.show()

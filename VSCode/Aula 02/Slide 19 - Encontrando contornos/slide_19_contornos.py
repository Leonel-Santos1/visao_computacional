# AULA 02 — SLIDE 19 — Encontrando contornos
# Coloque "binaria.png" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
binaria = cv2.imread("binaria.png", cv2.IMREAD_GRAYSCALE)
if binaria is None:
    raise FileNotFoundError('Coloque "binaria.png" na mesma pasta do código.')

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# drawContours é usado apenas para tornar visíveis os contornos encontrados.
# ------------------------------------------------------------
visualizacao = cv2.cvtColor(binaria, cv2.COLOR_GRAY2RGB)
cv2.drawContours(visualizacao, contornos, -1, (255, 0, 0), 2)
plt.imshow(visualizacao)
plt.title(f"Contornos externos encontrados: {len(contornos)}")
plt.axis("off")
plt.show()

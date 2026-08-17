# AULA 07 — SLIDE 07 — Salvando a imagem com as detecções
# Coloque "imagem.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
results = model.predict(
    source="imagem.jpg",
    save=True
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
if results:
    annotated = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title("Imagem com detecções")
    plt.axis("off")
    plt.show()

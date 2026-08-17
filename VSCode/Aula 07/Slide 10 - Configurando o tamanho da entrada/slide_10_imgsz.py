# AULA 07 — SLIDE 10 — Configurando o tamanho da entrada
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
    imgsz=640
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
if results:
    annotated = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title("Detecções com imgsz=640")
    plt.axis("off")
    plt.show()

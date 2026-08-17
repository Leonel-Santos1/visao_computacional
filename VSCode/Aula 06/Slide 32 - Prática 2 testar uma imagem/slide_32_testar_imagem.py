# AULA 06 — SLIDE 32 — Prática 2: testar uma imagem
# Coloque "imagem.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("yolo26n.pt")
results = model.predict(
    source="imagem.jpg",
    conf=0.25,
    save=True
)

for result in results:
    print(result.boxes)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# ------------------------------------------------------------
if results:
    annotated = results[0].plot()
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title("Resultado da inferência")
    plt.axis("off")
    plt.show()

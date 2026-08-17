# AULA 06 — SLIDE 29 — Como acessar as detecções produzidas?
# Coloque "imagem.jpg" nesta pasta antes de executar.

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")
results = model("imagem.jpg")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
for result in results:
    boxes = result.boxes

    xyxy = boxes.xyxy
    conf = boxes.conf
    cls = boxes.cls
    annotated = result.plot()

    result.save(filename="saida.jpg")

    # --------------------------------------------------------
    # PLOT / VISUALIZAÇÃO — apoio didático
    # O próprio código do slide já produz "annotated".
    # --------------------------------------------------------
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title("Detecções produzidas pelo YOLO")
    plt.axis("off")
    plt.show()

# AULA 09 — SLIDE 41 — Prática 4: teste o best.pt em imagens novas
# Tenha a pasta "imagens_novas" e o checkpoint no caminho indicado.

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
trained = YOLO(
    "runs_aula09/grupo_01_exp01/"
    "weights/best.pt"
)
results = trained.predict(
    source="imagens_novas",
    save=True,
    conf=0.25
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# Exibe os resultados processados para facilitar a revisão dos acertos e erros.
# ------------------------------------------------------------
for i, result in enumerate(results):
    annotated = result.plot()
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title(f"Imagem nova — resultado {i + 1}")
    plt.axis("off")
    plt.show()

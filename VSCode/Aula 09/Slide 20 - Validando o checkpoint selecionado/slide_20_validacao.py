# AULA 09 — SLIDE 20 — Validando o checkpoint selecionado
# Tenha "data.yaml" e o checkpoint no caminho indicado pelo slide.

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO(
    "runs_aula09/nano_640_exp01/"
    "weights/best.pt"
)
metrics = model.val(
    data="data.yaml",
    plots=True
)

print(metrics.box.map)
print(metrics.box.map50)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# plots=True salva gráficos da validação. Exibimos os mais comuns se existirem.
# ------------------------------------------------------------
save_dir = Path(metrics.save_dir)
for nome in ["PR_curve.png", "F1_curve.png", "confusion_matrix_normalized.png"]:
    caminho = save_dir / nome
    if caminho.exists():
        plt.figure(figsize=(8, 6))
        plt.imshow(mpimg.imread(caminho))
        plt.title(nome.replace("_", " ").replace(".png", ""))
        plt.axis("off")
        plt.show()

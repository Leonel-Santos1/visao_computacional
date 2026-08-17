# AULA 09 — SLIDE 39 — Prática 2: inicie o treinamento do grupo
# Tenha "data.yaml" e o dataset preparados conforme a Aula 08.

from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("yolo26n.pt")
results = model.train(
    data="data.yaml",
    epochs=20,
    imgsz=640,
    project="runs_aula09",
    name="grupo_01_exp01"
)

# ------------------------------------------------------------
# PLOT / VISUALIZAÇÃO — apoio didático
# O treinamento da Ultralytics salva o gráfico consolidado em results.png.
# ------------------------------------------------------------
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plot_path = Path(model.trainer.save_dir) / "results.png"
if plot_path.exists():
    plt.figure(figsize=(12, 6))
    plt.imshow(mpimg.imread(plot_path))
    plt.title("Curvas do treinamento")
    plt.axis("off")
    plt.show()

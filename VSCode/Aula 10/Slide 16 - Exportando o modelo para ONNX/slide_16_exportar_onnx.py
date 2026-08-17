# AULA 10 — SLIDE 16 — Exportando o modelo para ONNX
# Coloque "best.pt" nesta pasta antes de executar.

from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("best.pt")
exported_path = model.export(
    format="onnx"
)
print(exported_path)

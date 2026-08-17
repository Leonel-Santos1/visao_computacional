# AULA 06 — SLIDE 24 — Primeira inferência com Python
# Coloque "imagem.jpg" nesta pasta antes de executar.

from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("yolo26n.pt")
results = model("imagem.jpg")

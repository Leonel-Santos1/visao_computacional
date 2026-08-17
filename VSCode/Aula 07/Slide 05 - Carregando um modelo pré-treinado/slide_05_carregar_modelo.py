# AULA 07 — SLIDE 05 — Carregando um modelo pré-treinado

# APOIO PARA EXECUÇÃO — import necessário porque este arquivo é independente.
from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("yolo26n.pt")

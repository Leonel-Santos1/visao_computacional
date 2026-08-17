# AULA 09 — SLIDE 04 — Do zero ou a partir de um modelo pré-treinado?

from ultralytics import YOLO

# Treinamento do zero, como no slide.
modelo_do_zero = YOLO("yolo26n.yaml")

# Fine-tuning / transfer learning, como no slide.
modelo_pre_treinado = YOLO("yolo26n.pt")

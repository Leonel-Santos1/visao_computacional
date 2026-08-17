# AULA 07 — SLIDE 14 — Lendo os scores de confiança
# Coloque "imagem.jpg" nesta pasta antes de executar.

from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")
results = model("imagem.jpg")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
for result in results:
    print(result.boxes.conf)

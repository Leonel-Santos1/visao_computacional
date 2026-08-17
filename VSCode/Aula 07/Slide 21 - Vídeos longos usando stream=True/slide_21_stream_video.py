# AULA 07 — SLIDE 21 — Vídeos longos: usando stream=True
# Esta prática fica somente no VS Code.
# Coloque "video.mp4" nesta pasta antes de executar.

from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
results = model.predict(
    source="video.mp4",
    stream=True
)

for result in results:
    print(result.boxes)

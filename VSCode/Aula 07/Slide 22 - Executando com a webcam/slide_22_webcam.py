# AULA 07 — SLIDE 22 — Executando com a webcam
# Esta prática fica somente no VS Code.

from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
results = model.predict(
    source=0,
    show=True,
    stream=True
)

for result in results:
    pass

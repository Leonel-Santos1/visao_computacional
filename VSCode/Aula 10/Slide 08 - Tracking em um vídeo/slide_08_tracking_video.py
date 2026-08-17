# AULA 10 — SLIDE 08 — Tracking em um vídeo
# Esta prática fica somente no VS Code.
# Coloque "video.mp4" e "best.pt" nesta pasta antes de executar.

from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("best.pt")
results = model.track(
    source="video.mp4",
    show=True,
    save=True
)

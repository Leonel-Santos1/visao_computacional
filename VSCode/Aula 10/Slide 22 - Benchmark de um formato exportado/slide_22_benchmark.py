# AULA 10 — SLIDE 22 — Benchmark de um formato exportado
# Tenha "best.pt" e "data.yaml" disponíveis.

from ultralytics.utils.benchmarks import benchmark

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
benchmark(
    model="best.pt",
    data="data.yaml",
    imgsz=640,
    format="onnx"
)

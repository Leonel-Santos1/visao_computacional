# AULA 07 — SLIDE 31 — Desafio: contar uma classe específica
# Coloque "imagem.jpg" nesta pasta antes de executar.

from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")
results = model("imagem.jpg")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
alvo = "person"
contador = 0

for result in results:
    for box in result.boxes:
        cls_id = int(box.cls[0])
        nome = result.names[cls_id]

        if nome == alvo:
            contador += 1

print("Quantidade:", contador)

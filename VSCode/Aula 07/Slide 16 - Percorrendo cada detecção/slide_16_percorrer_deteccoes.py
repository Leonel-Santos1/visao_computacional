# AULA 07 — SLIDE 16 — Percorrendo cada detecção
# Coloque "imagem.jpg" nesta pasta antes de executar.

from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide.
model = YOLO("yolo26n.pt")
results = model("imagem.jpg")

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
for result in results:
    for box in result.boxes:
        classe_id = int(box.cls[0])
        confianca = float(box.conf[0])
        coordenadas = box.xyxy[0].tolist()

        # Apoio didático: imprime as variáveis criadas no trecho.
        print("classe_id:", classe_id)
        print("confianca:", confianca)
        print("coordenadas:", coordenadas)

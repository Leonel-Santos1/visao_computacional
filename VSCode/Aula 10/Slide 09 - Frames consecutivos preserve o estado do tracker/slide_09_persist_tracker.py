# AULA 10 — SLIDE 09 — Frames consecutivos: preserve o estado do tracker
# Esta prática fica somente no VS Code.
# Coloque "video.mp4" e "best.pt" nesta pasta antes de executar.

import cv2
from ultralytics import YOLO

# APOIO PARA EXECUÇÃO — o slide mostra apenas o trecho aplicado a um frame.
model = YOLO("best.pt")
cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    # --------------------------------------------------------
    # CÓDIGO DO SLIDE
    # --------------------------------------------------------
    result = model.track(
        frame,
        persist=True,
        tracker="botsort.yaml"
    )[0]

    # Apoio visual para acompanhar o tracking no VS Code.
    cv2.imshow("Tracking", result.plot())
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

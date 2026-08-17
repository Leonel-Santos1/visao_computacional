# AULA 10 — SLIDE 39 — Prática coletiva 1: tracking com webcam
# Esta prática fica somente no VS Code.
# Coloque "best.pt" nesta pasta antes de executar.

import cv2
from ultralytics import YOLO

# ------------------------------------------------------------
# CÓDIGO DO SLIDE
# ------------------------------------------------------------
model = YOLO("best.pt")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    result = model.track(frame, persist=True)[0]
    annotated = result.plot()
    cv2.imshow("Projeto final", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

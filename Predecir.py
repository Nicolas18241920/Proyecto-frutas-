from ultralytics import YOLO

model = YOLO("runs/segment/frutas_n50/weights/best.pt")
model.predict(source="fotos_ok", save=True, conf=0.4, device=0, name="mis_fotos2")
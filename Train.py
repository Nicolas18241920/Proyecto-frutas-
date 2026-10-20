from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model.train(
        data="ul://1-ermias/datasets/fruitssegmentationdataset",
        epochs=50,
        patience=15,       # se detiene si no mejora en 15 épocas
        imgsz=640,
        batch=16,
        workers=4,
        device=0,
        name="frutas_n50",
    )
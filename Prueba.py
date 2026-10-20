from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model.train(
        data="ul://1-ermias/datasets/fruitssegmentationdataset",
        epochs=1,
        imgsz=640,
        batch=8,
        workers=2,
        device=0,
    )
#Please read and follow the README.md file first
from ultralytics import YOLO

if __name__ == "__main__":
    CustomModel = YOLO("yolo11n.pt")

    TrainData = CustomModel.train(
        data=r"", #Inside the "" should be the directory where the yaml file is placed in your laptop
        epochs=30, #Depends on how many images you have |Usual range:30,64,120
        imgsz=640,
        batch=16,
        device="cpu",
        workers=2,
        exist_ok=True
    )

    Run = CustomModel.val()
    print("mAP50", Run.box.map50)
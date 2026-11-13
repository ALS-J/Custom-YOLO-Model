#Please read and follow the README.md file first
from ultralytics import YOLO

if __name__ == "__main__":
    CustomModel = YOLO(r"runs/detect/train/weights/best.pt") #Only run once you see the runs file 
                                                             #has evertyhing after running the YOLO train
    CustomModel.predict(source=0, show=True, conf=0.5)
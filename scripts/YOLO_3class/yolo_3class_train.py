# This script trains the model, that will be saved at runs/classify/train/weights/best.pt
import ultralytics

model = ultralytics.YOLO("yolo11n-cls.pt")

# Path to the folder that will have test and train
results = model.train(data="./data_folder", epochs=100, imgsz=640)


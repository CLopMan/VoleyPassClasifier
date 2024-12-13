# This script trains the model for 2 classes, that will be saved at runs/classify/train2/weights/best.pt
import ultralytics

# Load a trained model as a base for our model
model = ultralytics.YOLO("yolo11n-cls.pt")

# Path to the folder that will have test and train
results = model.train(data="./data_folder", epochs=100, imgsz=640)


from ultralytics import YOLO
import numpy as np

# Loading the trained model
model = YOLO("./runs/classify/train/weights/best.pt")

# The file we want to predict will be passed through input
input_predict = input("Introduce el fichero a predecir:")

predictions = model(input_predict, show=True, stream=True)

format = {   0: 'correct_set',
             1: 'wrong_set'}
correct = 0
wrong = 0
confidence = []


for prediction in predictions:
    top = prediction.probs.top1
    confidence.append(prediction.probs.top1conf)
    if(top == 1):
        correct +=1
    else:
        wrong +=1

print("RESULTADO: set correcto =", correct, " instancias, porcentaje = ", 100*(correct/(correct+wrong)), "%\n",
      "set incorrecto= ",wrong, "instancias, porcentaje =", 100*(wrong/(wrong+correct)), 
      "\nConfianza media:",np.mean(confidence),
      "Clase mayoritaria de clasificación:", max(correct,wrong))
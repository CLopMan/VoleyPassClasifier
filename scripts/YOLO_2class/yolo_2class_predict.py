from ultralytics import YOLO
import numpy as np

# Loading the trained model
model = YOLO("./runs/classify/train/weights/best.pt")

# The file we want to predict will be passed through input
input_predict = input("Introduce el fichero a predecir:")

predictions = model(input_predict, show=True, stream=True)

correct = 0
wrong = 0
confidence = []

# Counts instances of each class
for prediction in predictions:
    top = prediction.probs.top1
    confidence.append(prediction.probs.top1conf)
    if(top == 0):
        correct +=1
    else:
        wrong +=1

# Checks what class most of the frames are
if correct > wrong:
    clase_mayoritaria = "Set correcto"
elif wrong > correct:
    clase_mayoritaria = "Set incorrecto"
else:
    clase_mayoritaria = "no concluyente"

# results
print("RESULTADO: set correcto =", correct, " instancias, porcentaje = ", 100*(correct/(correct+wrong)), "%\n",
      "set incorrecto= ",wrong, "instancias, porcentaje =", 100*(wrong/(wrong+correct)), 
      "\nConfianza media:",np.mean(confidence),
      "Clase mayoritaria de clasificación:", clase_mayoritaria)
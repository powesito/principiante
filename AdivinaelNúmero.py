import random

numero = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número del 1 al 100: "))

    if intento < numero:
        print("Muy bajo")
    elif intento > numero:
        print("Muy alto")
    else:
        print("Correcto")
        break
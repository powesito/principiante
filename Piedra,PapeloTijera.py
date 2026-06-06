import random

opciones = ["piedra", "papel", "tijera"]

usuario = input("Elige piedra, papel o tijera: ").lower()
pc = random.choice(opciones)

print("La PC eligió:", pc)

if usuario == pc:
    print("Empate")
elif (
    (usuario == "piedra" and pc == "tijera") or
    (usuario == "papel" and pc == "piedra") or
    (usuario == "tijera" and pc == "papel")
):
    print("Ganaste")
else:
    print("Perdiste")


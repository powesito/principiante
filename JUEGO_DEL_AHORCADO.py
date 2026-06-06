import random


palabras = [
    "python",
    "programacion",
    "computador",
    "teclado",
    "internet"
]


palabra = random.choice(palabras)


intentos = 6

letras = []


print("🎮 JUEGO DEL AHORCADO")


while intentos > 0:


    mostrar = ""


    for letra in palabra:

        if letra in letras:
            mostrar += letra

        else:
            mostrar += "_"


    print("\nPalabra:", mostrar)


    if "_" not in mostrar:
        print("Ganaste 🎉")
        break


    letra = input("Ingresa letra: ").lower()


    if letra in letras:

        print("Ya usaste esa letra")

    elif letra in palabra:

        letras.append(letra)
        print("Correcto ✅")


    else:

        intentos -= 1
        letras.append(letra)

        print("Incorrecto ❌")
        print("Intentos:", intentos)



if intentos == 0:

    print("Perdiste 😢")
    print("La palabra era:", palabra)
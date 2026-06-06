texto = input("Escribe un texto:\n")

palabras = texto.split()

print("Cantidad de palabras:", len(palabras))

print("\nPalabras:")
for p in palabras:
    print(p)
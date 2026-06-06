import os
import shutil

carpeta = input("Ruta de carpeta: ")

archivos = os.listdir(carpeta)

for archivo in archivos:

    ruta = os.path.join(carpeta, archivo)

    if os.path.isfile(ruta):

        extension = archivo.split(".")[-1]

        nueva = os.path.join(carpeta, extension)

        if not os.path.exists(nueva):
            os.mkdir(nueva)

        shutil.move(
            ruta,
            os.path.join(nueva, archivo)
        )


print("Archivos organizados")
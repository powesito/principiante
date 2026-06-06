import random
import string

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(longitud):
    password += random.choice(caracteres)

print("Contraseña generada:", password)
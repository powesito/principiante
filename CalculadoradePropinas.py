#Calculadora de Propinas

cuenta = float(input("Ingrese el total de la cuenta: "))
propina = int(input("Ingrese el porcentaje de propina: "))

total_propina = cuenta * (propina / 100)
total_final = cuenta + total_propina

print("Propina:", total_propina)
print("Total a pagar:", total_final)
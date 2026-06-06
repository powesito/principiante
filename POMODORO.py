import time

minutos = int(input("Minutos de Pomodoro: "))

segundos = minutos * 60


while segundos > 0:

    m = segundos // 60
    s = segundos % 60

    print(f"{m:02d}:{s:02d}", end="\r")

    time.sleep(1)

    segundos -= 1


print("\n Tiempo terminado")
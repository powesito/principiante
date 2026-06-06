import tkinter as tk
import time

def reloj():
    hora = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora)
    etiqueta.after(1000, reloj)

ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("300x150")

etiqueta = tk.Label(
    ventana,
    font=("Arial",40),
    bg="black",
    fg="lime"
)

etiqueta.pack(expand=True)

reloj()

ventana.mainloop()
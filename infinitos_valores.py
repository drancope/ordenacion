# Ordenar cuatro valores en lista.
# Para obtener la lista usamos una interfaz interactiva

#Aquí empieza la inicialización
import tkinter as tk

n = []


# funciones reutilizables
def swap(i):
    a= n[i]
    n[i] = n[i+1]
    n[i+1] = a
    
def agregarNumero():
    global n
    n.append(int(numero.get()))


def ordenar():
    contador = 0
    bucles = 0
    for i in range(len(n)-1):
        yaEsta = 0
        for j in range(len(n)-1):
            bucles = bucles +1
            if (n[j] > n[j+1]):
                swap(j)
                yaEsta = 1
                contador = contador +1
        if yaEsta == 0:
            break

    print(n)
    print("Número de intercambios: ", contador, " en ", bucles, " bucles")

root = tk.Tk()

label = tk.Label(text="Número: ")
numero = tk.Entry()
button1 = tk.Button(text="Añadir", command=agregarNumero)
button2 = tk.Button(text="Ordenar", command=ordenar)
button3 = tk.Button(text="Salir", command=root.destroy)
label.pack()
numero.pack()
button1.pack()
button2.pack()
button3.pack()


root.mainloop()

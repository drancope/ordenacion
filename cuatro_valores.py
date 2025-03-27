# Ordenar cuatro valores en lista.
# Para obtener la lista usamos una interfaz interactiva

#Aquí empieza la inicialización
import ipywidgets as widgets

widgets.IntText(
    value=7,
    description='Any:',
    disabled=False
)
n = []

# funciones reutilizables
def swap(n):
    a= n[0]
    n[0] = n[1]
    n[1] = a

# Toma de datos
for i in range(4):
    n.append()
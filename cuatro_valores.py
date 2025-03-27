# Ordenar cuatro valores en lista.
# Para obtener la lista usamos una interfaz interactiva

#Aquí empieza la inicialización
import ipywidgets as widgets
from IPython.display import display 

numero = widgets.IntText(
    value=7,
    description='Any:',
    disabled=False
)
n = []
boton = widgets.Button(description="aceptar")


# funciones reutilizables
def swap(n):
    a= n[0]
    n[0] = n[1]
    n[1] = a

pulsado = 0
def dar_ok():
    pulsado = 1

boton.on_click(dar_ok)

# Toma de datos
display(numero, boton)
for i in range(4):
    if pulsado:
        n.append(numero.value)
    pulsado=0

print(n)
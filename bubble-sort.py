######
# Archivo: Buuble-sort.py
# Fecha: 14/04/2025
# Lee un archivo txt y lo imprime ordenado
######

n =[]

# funciones reutilizables
def swap(i):
    a= n[i]
    n[i] = n[i+1]
    n[i+1] = a
    
def agregarNumero(linea):
    global n
    n.append(int(linea))

### Inicio del programa principal:

# Leer el archivo y agregar cada línea
f = open("datos.txt", "r")
for linea in f:
    n.append(int(linea))
# Copiar n a s, ordenar.
s = n
for i in range(len(n)-1):   #Aquí hacemos el repaso a la lista dos veces
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            swap(j)
print(s)

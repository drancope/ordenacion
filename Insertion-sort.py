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
print(s)
for i in range(len(s)-1):
    pared = s[i+1]
    j = i
    while (j>=0 and s[j]>pared):
        s[j+1] = s[j]
        j = j-1
    s[j+1] = pared
print(s)  
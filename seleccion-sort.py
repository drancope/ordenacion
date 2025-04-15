######
# Archivo: seleccion-sort.py
# Fecha: 14/04/2025
# Lee un archivo txt y lo imprime ordenado
# por el método de selección
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
    a = s[i]
    for j in range(i+1, len(s)):
        if a > s[j]:
            a = s[j]        
            aux = s[i]
            s[i] = s[j]
            s[j] = aux
print(s)

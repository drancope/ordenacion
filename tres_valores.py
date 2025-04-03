# Ordenar crecientemente una lista de tres valores.
# Existe un error, ya que según los valores, puede cambiar
# dos que entre ellos había que cambiar, pero genera mal orden
# en los posteriores.

n = []

for i in range(6):
    n.append(int(input()))

s = n
for i in range(5):    #Aquí se refleja el error p.ej. con [7, 5, 3]
    if s[i] > s[i+1]:
        a = s[i]
        s[i] = s[i+1]
        s[i+1] = a
print(s)

s = n
for i in range(len(n)-2):   #Aquí hacemos el repaso a la lista dos veces
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            a = s[j]
            s[j] = s[j+1]
            s[j+1] = a
print(s)
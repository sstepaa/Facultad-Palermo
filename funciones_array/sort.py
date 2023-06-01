#Esta funcion permite ordenar elemento de forma creciente 
a = []

n = int(input('Ingrese la cantidad de elemento que necesite el arreglo'))

for i in range(0 , n):
    a.append(int(input('Ingrese el valor de cada elemento')))

a.sort()

for i in range(0 , n):
    print(a[i])

#Para ordenar el array de forma decreciente se puede usar el sort con un reverse

a.sort(reverse=True)
for i in a:
    print(i)
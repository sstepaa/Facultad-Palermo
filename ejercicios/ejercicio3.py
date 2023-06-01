#Dados dos arreglos A y B de N<15 elementos cada uno, calcular un arreglo C tal que C = A + B.

a = []
b = [] 
c = []

n = int(input('Ingrese la cantidad de elemento de los array'))

for i in range(0 , n):
    a.append(int(input('Ingrese el valor del elemento para el array A ')))

    b.append(int(input('Ingrese el valor del elemento para el array B ')))

c = a + b

print(c)
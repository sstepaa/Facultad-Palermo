#Esta funcion permite eliminar un elemento determinado del array

a = []
n = int(input("Ingrese la cantidad de elemento que quiere que contenga el array"))

for i in range(0 , n):
    a.append(int(input('Ingrese un elemento del array')))
a.remove(3)#Elimina el primer 3 que encuentre en el array

for i in a:
    print(i)
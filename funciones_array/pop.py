a = []
n = int(input("Ingrese la cantidad de elemento que quiere que contenga el array"))

for i in range(n):
    a.append(int(input('Ingrese un elemento del array')))


elemento_eliminado = a.pop(3)#Elimina el primer 3 que encuentre en el array y lo devuelve

for i in a:
    print(i)

print('elemento eliminado' , elemento_eliminado)
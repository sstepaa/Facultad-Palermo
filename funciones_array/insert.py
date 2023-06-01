#Esta funcion permite insertar un valor enn una posición determinada de un arreglo
#nombreDelArray.insert(posicion , valor)


#ingresar un arreglo de n elementos y un valor y la posición en la que desea insertarese valor. Mostrar el nuevo arreglo

a = []
n = int(input('Ingrese la cantidad de elementos del array'))


#Este for es para recorrer la cantidad de elementos que querramos que tenga el array
for i in range(n):
    a.append(int(input('Ingrese el valor de cada elemento')))

m = int(input('Ingrese el valor a insertar'))

pos = int(input("Ingrese la posición donde va a insertar el numero"))
a.insert(pos, m)
#¿Por que n+1?
#Cuando utilizas el bucle for i in range(n+1), estás generando un rango que va desde 0 hasta n inclusive. Sin embargo, dado que los índices válidos de un array van hasta n-1, intentar acceder al elemento en la posición n causará un error de índice fuera de rango.
for i in range(0 , n+1):
    print(a[i])



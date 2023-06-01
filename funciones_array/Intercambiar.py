#Intercambiar dos elementos en un mismo array
#Se deben conocer bien las dos posiciones que se quieren cambiar 

a = [ 1 , 2 , 3 , 4 , 5]

#Indices de los elementos a intercambiar
indice1 = 1
indice2 = 2

#Se imprime el array común
print(f'Array antes del intercambio {a}')

#Intercambia los elementos
a[indice1] , a[indice2] = a[indice2] , a[indice1]

#Array intercambiado
print(f'Asi queda el array con la instruccion de intercambio {a}')
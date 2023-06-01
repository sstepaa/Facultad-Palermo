#Ingresar un arreglo de 10 componentes:
# a. Imprimir la cuarta componente.
# b. Imprimir las componentes en orden invertida.
# c. Imprimir el producto entre la primera y la última componente.
# d. Imprimir las componentes de índice impar.
# e. Imprimir la suma de las componentes de índice par.
# f. Imprimir la multiplicación de las componentes de índice impar.
# g. Imprimir el arreglo que resulta de intercambiar la primera con la últimacomponente

a = [1 , 2 , 3 , 4 , 5 ,6 , 7 , 8 , 9 , 10] #array de 10 componentes
#a. Imprimir el cuarto componente 
print(a[3]) 
#b Imprime el array al reverso
a.reverse()
print(a) 

#c. Imprimir el producto entre la primera y la última componente.
element_1 = a[0]
element_last = a[9]

print(element_1 * element_last)

#d. Imprimir las componentes de índice impar.
new_array = []

for i in a:
    if i % 2 == 0:
          new_array.append(i)

print(new_array)

#e Imprimir la suma de las componentes de índice par.
suma = 0
for i in new_array:
    suma = suma + i

print(suma)

#f. Imprimir la multiplicación de las componentes de índice impar.
multiplicación = 1
for i in new_array:
    multiplicación = multiplicación * i

print(multiplicación)

#g. Imprimir el arreglo que resulta de intercambiar la primera con la última componente
a[0] , a[9] = a[9] , a[0]
#Imprimo el array intercambiado
print(a)

a = []
n = int(input('Ingrese un numero de iteraciones'))

for i in range(0 , n):
    #Agregamos elementos al array
    a.append(int(input('Ingrese un elemento del array')))
#Con el for este recorremos el array elemento por elemento
for i in range(0 , n):
    print('elemento' , a[i])
i = 0 
while (i < n and a[i] % 3 != 0): 
    i = i + 1

if i == n :
    print("El vector no tiene ningún elemento múltiplo de 3")
else:
    print(f"El primer multiplo de 3 esta en la posición {i} y es {a[i]}")
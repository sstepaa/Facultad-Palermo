#Definir un array en python se puede hacer de la siguiente manera 
a = ['hola' , 'two' , 'three'] 
#Es un array de 3 elementos , recorda que las posiciones de un array se cuentan desde el número 0
for i in range(0 , 3) : 
    print(a[i])

#Cuando trabajamos con variables de este tipo podemos realizar cargar , recorrer , mostrar , buscar elementos , desplazar , intercambiar y ordenar. 

#Cargar elementos en un array vacío
b = [] 
n = int(input('Ingrese elementos en el array'))
sumar = 0 #Si inicializamos aca la variable vamos a sumar todos los elementos adentro de array
for i in range (0 , n) : 
    #sumar = 0 no se inicializa aca la variable xq en cada iteracion del bucle vamos a guardar solo la suma del ultimo número pasado
    #La funcion append agrega cada elemento que se pide en el input , en el array con nombre b.
    b.append(int(input('Ingrese el valor de cada elemento')))    
    sumar = sumar + b[i]
print(b)
print(sumar)


    

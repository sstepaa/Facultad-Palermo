def suma_divisores(numero): 
    #En esta funcion obtuve la suma de los divisores del numero pasado
    suma = 0
    for i in range(1 , int(numero**0.5)+1):
        if numero % i == 0:
            suma += i
            complemento = numero // i
            if complemento != i: 
                suma += complemento
    return suma


def numeros_amigos(num1 , num2):
    if (suma_divisores_una == num2 and suma_divisores_dos == num1) :
        return True
    else :
        return False

#Pide los números
numero1 = int(input('Ingrese un numero : '))
numero2 = int(input('Ingrese un numero : '))

#variables que guardan las suma de divisores de cada uno de los numero pedidos 
suma_divisores_una = suma_divisores(numero1)
suma_divisores_dos = suma_divisores(numero2)

if numeros_amigos(numero1, numero2):
    print(f'Los números {numero1} y {numero2} son amigos')
else:
    print(f'Los números {numero1} y {numero2} no son amigos')

print(f'La suma de los divisores es : {suma_divisores_una}')
print(f'La suma de los divisores es : {suma_divisores_dos}')
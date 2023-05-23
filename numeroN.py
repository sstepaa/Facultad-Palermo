def mitadPar(n): 
    #Es imprecindible inicializar la variale en 0 
    num_par_mitad = 0
    #Convertir el argumento en tipo de dato integer 
    if int(n) % 2 == 0 :
        num_par_mitad = int(n) / 2
        #Convertir el argunmento en int
    return num_par_mitad

numero = input('ingrese un numero')
resultado = mitadPar(numero)
print(f'El resultado de la mitad del numero par es {resultado}')
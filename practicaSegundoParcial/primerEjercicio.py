nombre = str()
apellido = str()
max_saldo_caja_ahorro = int()
acum = int()
nombre_max = str()

#Pedir nombre y apellido para entrar en la condicion del while
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")

while nombre != "fin" and apellido != "fin" : 
    acum = 0
    max_saldo_caja_ahorro = 0
    saldo_caja_ahorro = int(input("Ingrese su cantidad de dinero que posee en su caja de ahorros"))
    saldo_caja_corriente = int(input("Ingrese su cantidad de dinero que posee en su caja corriente"))
        
        
    if saldo_caja_ahorro < 0 or saldo_caja_corriente < 0 :
            acum = acum + 1
    

    """if saldo_caja_ahorro > max_saldo_caja_ahorro  : 
        max_saldo_caja_ahorro = saldo_caja_ahorro
        nombre_max = nombre"""
    nombre = input("Ingrese su nombre")
    apellido = input("Ingrese su apellido")

#fin del while    
    
if nombre == "fin" and apellido == "fin" :
    """print(f"{nombre_max} usted tiene mayor cantidad de saldo en la caja de ahorro {max_saldo_caja_ahorro}")"""
    print(f'Clientes con salgo negativo {acum}')

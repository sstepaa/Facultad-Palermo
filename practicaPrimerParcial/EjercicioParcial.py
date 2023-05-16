#En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio: 

#Diseñar un programa en Python que permita:

#Una cadena de hoteles cuenta con 10 filiales y necesita obtener algunas estadísticas para mejorar sus servicios. Para ello se ingresan:

#Nombre de la ciudad de la filial
#Capacidad total del hotel (en cuanto a huéspedes)
#Cantidad de habitaciones
#Cantidad de huéspedes en un mes.
#Calcular y mostrar:

#Cantidad de huéspedes que puede alojar toda la cadena de hoteles.
#Porcentaje de ocupación de cada hotel.
#El nombre de la ciudad con la mayor cantidad de habitaciones. 

#Declarar las variables contadoras 
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
cont10 = 0

#Declarar variable para buscar el maximo d habitaciones
max = 0

#declarar variable porcentaje
porc = 0

for i in range (1 , 3 , 1):
    #Listo todas las funcionalidades , agregar las otras 8 iteraciones y mejorar las salidas por pantallas.
        nombre_filial = str(input("Ingrese el nombre el hotel"))
        cant_habitaciones = int(input("Ingrese la cantidad de habitaciones "))
        cant_total_huesped = int(input("Ingrese la cantidad total de huespedes que pueda alojar el hotel"))
        cant_actual_huesped = int(input("Ingrese la cantidad actual de huespedes"))
        
        if i == 1 : 
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        
        cont1 =+ cant_total_huesped
    
        if i == 2 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
            
        cont2 =+ cant_total_huesped

        if i == 3 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont3 =+ cant_total_huesped

        if i == 4 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont4 =+ cant_total_huesped

        if i == 5 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont5 =+ cant_total_huesped
    
        if i == 6 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont6 =+ cant_total_huesped

        if i == 7 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont7 =+ cant_total_huesped

        if i == 8 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont8 =+ cant_total_huesped

        if i == 9 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))
            print("Porcentaje de ocupación " , porc , "%")
        cont9 =+ cant_total_huesped

        if i == 10 :
            porc = float(round((cant_actual_huesped * 100) / cant_total_huesped , 2))        
            print("Porcentaje de ocupación " , porc , "%")
        cont10 =+ cant_total_huesped
    
    #se consigue el valor maximo
        if cant_habitaciones > max :
            max = cant_habitaciones
            nombre_filial_max = nombre_filial

        nombre_filial = str(input("Ingrese el nombre el hotel"))
        cant_habitaciones = int(input("Ingrese la cantidad de habitaciones "))
        cant_total_huesped = int(input("Ingrese la cantidad total de huespedes que pueda alojar el hotel"))
        cant_actual_huesped = int(input("Ingrese la cantidad actual de huespedes"))
        
    
    

cont_total = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print("mayor habitaciones " , max , "Su hotel es el : " , nombre_filial_max)
print("Cantidad total de huespedes " , cont_total)

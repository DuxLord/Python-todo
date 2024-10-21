############################################
# UNIDAD 1 - Ejercicio 4                   #
# Diccionario vuelo (ESQUEMA)              #
############################################

vuelo = {'origen':'Valencia', 'destino':'Menorca', 'día':'15-08', 'clase':'turista'}
acaba = False
while not acaba:
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in ['1', '2', '3', '4', '5', '0']:
        print()
        print("=========================")            
        print("   GESTIÓN DE UN VUELO   ")
        print("=========================")
        print(" 1 - Imprimir datos vuelo")
        print(" 2 - Imprimir claves ")
        print(" 3 - Añadir <pasajeros> ")        
        print(" 4 - Imprimir un valor")
        print(" 5 - Borrar clave ")
        print(" 0 - SALIR ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        print()

    #Respondemos a la opción seleccionada    
    if opcion == '1':  #Imprimir datos del diccionario
        print("DATOS DEL VUELO:")
        pass
    elif opcion == '2': #Imprimir las claves del diccionario
        print("CLAVES: ", end='')
        pass
    elif opcion == '3': #Añadir la clave 'pasajeros' con su valor
        pass
    elif opcion == '4': #Dada una clave, imprimir un valor
        pass
    elif opcion == '5': #Borrar una clave con su valor
        pass
    else:
        acaba = True        
    
print("Hasta pronto")
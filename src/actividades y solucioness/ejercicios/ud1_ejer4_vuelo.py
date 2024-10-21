############################################
# UNIDAD 4 - Ejercicio 4                   #
# Diccionario vuelo (SOLUCIÓN)             #
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
        #print(vuelo)        
        for k, v in vuelo.items():
            print(k, '-->', v)
        print()
    elif opcion == '2': #Imprimir las claves del diccionario
        print("CLAVES: ", end='')
        for k in vuelo.keys():
            print(k, end=', ')
        print('\n')
    elif opcion == '3': #Añadir la clave 'pasajeros' con su valor
        valor = int(input("Dame el nº de pasajeros: "))
        vuelo["pasajeros"] = valor        
        print("Nº de pasajeros actualizado")                        
    elif opcion == '4': #Dada una clave, imprimir un valor
        clave = input("¿Qué clave quieres consultar? ")
        valor = vuelo.get(clave)
        if valor is None:
            print("Lo siento pero la clave no existe")
        else:
            print(clave, '-->', valor)        
    elif opcion == '5': #Borrar una clave con su valor
        clave = input("¿Qué clave quieres borrar? ")
        valor = vuelo.pop(clave, "error")
        if valor == "error":
            print("Lo siento pero la clave no existe")
        else:
            print(clave, '-->', valor)
    else:
        acaba = True        
    
print("Hasta pronto")

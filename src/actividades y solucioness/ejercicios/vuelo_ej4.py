############################################
# UNIDAD 1 - Ejercicio 4           Gabriel #
# Diccionario vuelo (ESQUEMA)   Cardona    #
############################################

# Diccionario inicial del vuelo
vuelo = {
    'origen': 'Valencia',
    'destino': 'Menorca',
    'día': '15-08',
    'clase': 'turista'
}

# Bandera para terminar el programa
acaba = False

# Bucle principal del programa
while not acaba:
    # Mostrar menú y solicitar la operación al usuario
    opcion = ''
    while opcion not in ['1', '2', '3', '4', '5', '0']:
        print()
        print("=========================")
        print("   GESTIÓN DE UN VUELO   ")
        print("=========================")
        print(" 1 - Imprimir datos del vuelo")
        print(" 2 - Imprimir claves")
        print(" 3 - Añadir <pasajeros>")
        print(" 4 - Imprimir un valor")
        print(" 5 - Borrar clave")
        print(" 0 - SALIR")
        print("-----------------------------")
        opcion = input("Dame la opción: ")
        print()

    # Respondemos a la opción seleccionada
    if opcion == '1':  # Imprimir todos los datos del diccionario
        print("DATOS DEL VUELO:")
        for clave, valor in vuelo.items():
            print(f"{clave}: {valor}")

    elif opcion == '2':  # Imprimir solo las claves del diccionario
        print("CLAVES: ", list(vuelo.keys()))

    elif opcion == '3':  # Añadir la clave 'pasajeros' con su valor
        pasajeros = input("Introduce el número de pasajeros: ")
        vuelo['pasajeros'] = pasajeros
        print(f"Se ha añadido la clave 'pasajeros' con el valor {pasajeros}.")

    elif opcion == '4':  # Dada una clave, imprimir el valor asociado
        clave = input("Introduce el nombre de la clave: ")
        if clave in vuelo:
            print(f"El valor de '{clave}' es: {vuelo[clave]}")
        else:
            print("Error: la clave no existe en el diccionario.")

    elif opcion == '5':  # Borrar una clave y su valor
        clave = input("Introduce la clave que quieres borrar: ")
        if clave in vuelo:
            del vuelo[clave]
            print(f"Se ha borrado la clave '{clave}'.")
        else:
            print("Error: la clave no existe en el diccionario.")

    elif opcion == '0':  # Terminar el wprograma
        acaba = True

print("Hasta pronto")

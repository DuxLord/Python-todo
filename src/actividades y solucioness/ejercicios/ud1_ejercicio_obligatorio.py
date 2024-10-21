############################################
# UNIDAD 1 - Ejercicio obligatorio         #
# Lista de vuelos (ESQUEMA)                #
############################################

"""
Author: Gabriel Cardona Medina
Date: 19/09/2024
"""

# Información de los vuelos
vuelos = [{'origen':'Valencia', 'destino':'Menorca', 'día':'15-08', 'clase':'turista'},
          {'origen':'Valencia', 'destino':'Tenerife', 'día':'20-08', 'clase':'turista'},
          {'origen':'París', 'destino':'Valencia', 'día':'15-08', 'clase':'primera'},
          {'origen':'Atenas', 'destino':'Valencia', 'día':'20-08', 'clase':'primera'} ]

# Imprimir todos los vuelos
def imprimir(vuelos):
    print("==============================")
    print("Lista de vuelos:")
    for vuelo in vuelos:
        print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Día: {vuelo['día']}, Clase: {vuelo['clase']}")
1
# Buscar vuelos por origen
def buscar_origen(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    encontrado = False
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower():
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Día: {vuelo['día']}, Clase: {vuelo['clase']}")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún vuelo con ese origen.")
    print()

# Imprimir un vuelo por origen y destino
def imprimir_vuelo(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    encontrado = False
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Día: {vuelo['día']}, Clase: {vuelo['clase']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún vuelo con ese origen y destino.")
    print()

# Cambiar la fecha de un vuelo
def cambiar_fecha(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    encontrado = False
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            nueva_fecha = input(f"Introduce la nueva fecha para el vuelo de {origen} a {destino} (actual: {vuelo['día']}): ")
            vuelo['día'] = nueva_fecha
            print("Fecha modificada con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún vuelo con ese origen y destino.")
    return vuelos

# Menú
def menu():
    while True:
        print("""==============================
 GESTIÓN DE VUELOS
==============================
 1 - Imprimir todos los vuelos
 2 - Buscar vuelos por origen
 3 - Imprimir vuelo por origen y destino
 4 - Cambiar la fecha de un vuelo
 0 - SALIR
==============================""")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            imprimir(vuelos)
        elif opcion == '2':
            buscar_origen(vuelos)
        elif opcion == '3':
            imprimir_vuelo(vuelos)
        elif opcion == '4':
            cambiar_fecha(vuelos)
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción del menú.")

# Ejecución
menu()

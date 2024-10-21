jugadores = ["admin"]

def nuevoJugador():
    user = input("¿Cómo te llamas?: ")
    jugadores.append(user)

def seVaJugador():
    if len(jugadores) > 0:
        print(f"Adiós {jugadores.pop(0)}")
    else:
        print("No hay jugadores conectados.")

while True:
    print(f"\nJugadores conectados: {jugadores}")
    print("""
==========================
     JUGADORES ON-LINE
==========================
 1 - Llega un jugador nuevo
 2 - Se va un jugador
 3 - FIN
--------------------------""")

    while True:
        try:
            opcion = int(input("Dame una opción (1-3): "))
            if opcion not in (1, 2, 3):
                raise ValueError("Opción fuera de rango")
        except ValueError as e:
            print(f"\nError: {e}.\n Ingrese un número válido (1-3)")
        else:
            break

    if opcion == 1:
        nuevoJugador()
    elif opcion == 2:
        seVaJugador()
    elif opcion == 3:
        print("Saliendo del juego. ¡Hasta luego!")
        exit()

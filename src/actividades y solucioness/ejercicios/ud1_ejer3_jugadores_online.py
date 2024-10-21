###################################
# UNIDAD 1 - Ejercicio 3          #
# Jugadores on-line (SOLUCIÓN)    #
###################################

#Creamos la lista con todos los jugadores on-line que hay conectados
jugadores = ["mario", "mafalda", "luigi", "esther", "heidi", "songoku", "beauty", "beast"]
#Imprimimos la lista de jugadores on-line
print("LISTA DE JUGADORES: ", end=" ")    
for i in range(len(jugadores)):
    print(jugadores[i], "-", end=" ")        
print()    

acaba = False
while not acaba:
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in ['1', '2', '3']:
        print()
        print("===========================")            
        print("     JUGADORES ON-LINE     ")
        print("===========================")
        print(" 1 - Llega un jugador nuevo")
        print(" 2 - Se va un jugador")
        print(" 3 - FIN ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        print()

    #Respondemos a la opción seleccionada
    
    if opcion == '1':
        nombre = input("¿Quién eres? ")
        print("Bienvenid@ jugador", nombre)
        jugadores.append(nombre)
    elif opcion == '2':
        if len(jugadores) > 0:
            print("Adiós al jugador", jugadores.pop(0))
            print()
        else:
            print("No hay jugadores on-line en estos momentos.")
    else:
        acaba = True        
    
    #Imprimimos la lista de jugadores on-line
    print("LISTA DE JUGADORES: ", end=" ")    
    for i in range(len(jugadores)):
        print(jugadores[i], "-", end=" ")        
    print()    
    
print("Hasta pronto")
print()
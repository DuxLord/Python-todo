############################################
# UNIDAD 1 - Ejercicio 2                   #
# Validar opción de menú (SOLUCIÓN)        #
############################################

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while ((opcion < '0') or (opcion > '5')):
        print()
        print("=============================")            
        print("   GAMIFICACIÓN EN EL AULA   ")
        print("=============================")
        print(" 1 - Cargar datos del fichero")
        print(" 2 - Imprimir datos ")
        print(" 3 - Jugar ")
        print(" 4 - Guardar datos ")
        print(" 5 - Cambiar contraseña ")
        print(" 0 - SALIR ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        if ((opcion < '0') or (opcion > '5')):
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion

# PROGRAMA PRINCIPAL -------------------------------------------
opcion = valida_opcion()
print("La opción seleccionada es:", opcion)
input()
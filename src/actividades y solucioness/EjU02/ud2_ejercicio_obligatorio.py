########################################
# UNIDAD 2 - Ejercicio obligatorio     #
# Credenciales de jugadores (ESQUEMA)  #
########################################
import sqlite3

'''
Gabriel Cardona Medina
'''

conexion = sqlite3.connect('ejer_obligatorio.db')  #Creamos la conexión a la base de datos
cursor = conexion.cursor()  #Creamos el cursor

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    """Función que muestra un menú y valida que la opción sea correcta"""

    opc_correctas = ['1', '2', '3', '4', '5', '0']

    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("==================================")
        print("     CREDENCIALES JUGADORES       ")
        print("==================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Validar credencial ")
        print(" 3 - Cambiar credencial ")
        print(" 4 - Insertar nuevo jugador ")
        print(" 5 - Borrar jugador ")
        print(" 0 - SALIR ")
        print("--------------------------")
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()
    return opcion


def imprimir_jugadores(cursor):
    """Imprimir jugadores existentes en la base de datos

       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("IMPRIMIR JUGADORES")
    cursor.execute("SELECT Nombre, Vida FROM JUGADORES")  # Especifica las columnas que deseas
    t = cursor.fetchone()
    while t is not None:
        nombre, vida = t  # Asigna los valores a las variables
        print(f"Nombre: {nombre} - Vida: {vida}")  # Imprime en el formato deseado
        t = cursor.fetchone()  # siguiente registro



def existe_jugador(cursor, jugador):
    """Comprueba si existe un jugador en la tabla JUGADORES.

       Parámetros de entrada: cursor de la bd y nombre del jugador
       Parámetros de salida: devuelve True si existe y False en otro caso
    """
    cursor.execute("SELECT Nombre FROM JUGADORES WHERE Nombre = ?", (jugador,))
    return cursor.fetchone() is not None


def lee_vida():
    """Pide el valor "vida" por pantalla.

       Parámetros de entrada: no hay
       Parámetros de salida: número entero vida
    """
    correcto = False
    while not correcto:
        try:
            vida = int(input("Dame vida: "))
        except ValueError:
            print("Estábamos esperando un número entero. Por favor, vuelve a intentarlo.")
        else:
            correcto = True
    return vida


def existe_credencial(cursor, usuario, contras):
    """Comprueba si existe una credencial en la tabla CREDENCIALES.

       Parámetros de entrada: cursor de la bd, usuario y contraseña.
       Parámetros de salida: devuelve True si existe y False en otro caso

    """
    cursor.execute("SELECT usuario, contrasenya FROM CREDENCIALES WHERE usuario = ? and contrasenya = ?", (usuario,contras))
    return cursor.fetchone() is not None


def validar_credencial(cursor):
    """Comprueba si existe el par jugador-contrasenya.

       Parámetros de entrada: cursor de la bd
       Parámetros de salida: no hay
    """
    print("VALIDAR CREDENCIAL")
    a=input("Dame jugador: ")
    b=input("Dame contraseña: ")
    if existe_credencial(cursor,a,b):
        print(f"[{a}/{b}] sí es una credencial válida")
    else:
        print(f"[{a}/{b}] no es una credencial válida")


def cambiar_credencial(conexion, cursor):
    """Modifica la contraseña de un jugador

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("CAMBIAR CREDENCIAL")
    usuario = input("Dame jugador: ")

    # Comprobamos si el usuario existe
    if not existe_jugador(cursor, usuario):
        print(f"El jugador {usuario} no existe.")
        return

    # Pedimos la vieja contraseña
    vieja_contras = input("Dame la vieja contraseña: ")

    # Validamos la credencial con la contraseña actual
    if existe_credencial(cursor, usuario, vieja_contras):
        # Si la credencial es válida, pedimos la nueva contraseña
        nueva_contras = input("Dame la nueva contraseña: ")
        cursor.execute("UPDATE CREDENCIALES SET contrasenya = ? WHERE usuario = ?", (nueva_contras, usuario))
        conexion.commit()
        print(f"La contraseña del jugador {usuario} ha sido actualizada.")
    else:
        print("Contraseña incorrecta")



def insertar_jugador(conexion, cursor):
    """Inserta un nuevo jugador y su credencial en la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("INSERTAR JUGADOR")
    nombre = input("Dame el nombre del jugador: ")
    if existe_jugador(cursor, nombre):
        print("El jugador ya existe.")
        return

    vida = lee_vida()  # Pide la vida al jugador
    contras = input("Dame la contraseña del jugador: ")

    # Insertamos en la tabla JUGADORES
    cursor.execute("INSERT INTO JUGADORES (Nombre, Vida) VALUES (?, ?)", (nombre, vida))
    # Insertamos en la tabla CREDENCIALES
    cursor.execute("INSERT INTO CREDENCIALES (usuario, contrasenya) VALUES (?, ?)", (nombre, contras))

    conexion.commit()
    print(f"Jugador {nombre} ha sido insertado correctamente.")


def borrar_jugador(conexion, cursor):
    """Borra el jugador y sus credenciales de la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("BORRAR JUGADOR")
    nombre = input("Dame el nombre del jugador a borrar: ")

    if not existe_jugador(cursor, nombre):
        print(f"El jugador {nombre} no existe.")
        return

    # Eliminamos al jugador de ambas tablas
    cursor.execute("DELETE FROM JUGADORES WHERE Nombre = ?", (nombre,))
    cursor.execute("DELETE FROM CREDENCIALES WHERE usuario = ?", (nombre,))

    conexion.commit()
    print(f"El jugador {nombre} y sus credenciales han sido eliminados correctamente.")


# PROGRAMA PRINCIPAL -------------------------------------------

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1':  #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2':  #Validar credencial
        validar_credencial(cursor)
    elif opcion == '3':  #Cambiar credencial
        cambiar_credencial(conexion, cursor)
    elif opcion == '4':  #Insertar nuevo jugador
        insertar_jugador(conexion, cursor)
    elif opcion == '5':  #Borrar jugador
        borrar_jugador(conexion, cursor)
    opcion = valida_opcion()
conexion.close()

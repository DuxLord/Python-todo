import sqlite3
from datetime import datetime

# Función para convertir la fecha ingresada por el usuario al formato 'YYYY-MM-DD'
def formatear_fecha(fecha_str: str) -> str:
    """
    Función para convertir la fecha ingresada por el usuario al formato 'YYYY-MM-DD'
    :return: str
    """

    # fecha a objeto datetime
    try:
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')  # Cambia este formato si el usuario lo ingresa de forma diferente
        # formateada en 'YYYY-MM-DD'
        return fecha.strftime('%Y-%m-%d')
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, usa el formato DD/MM/YYYY.")
        return None

# Crear conexión a la base de datos en memoria
con = sqlite3.connect(":memory:")
cur = con.cursor()

# Crear tabla 'amigos'
cur.execute('''
    CREATE TABLE amigos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        fecha_naz TEXT
    )
''')


def ingresar_amigos():
    """
    Función para pedir datos al usuario e insertar en la base de datos
    :return: None
    """
    while True:
        nombre = input("Introduce el nombre del amigo: ")
        fecha_nacimiento = input("Introduce la fecha de nacimiento (DD/MM/YYYY): ")

        # Validar y formatear la fecha antes de insertarla
        fecha_naz_str = formatear_fecha(fecha_nacimiento)
        if fecha_naz_str:
            cur.execute("INSERT INTO amigos (nombre, fecha_naz) VALUES (?, ?)", (nombre, fecha_naz_str))
        else:
            continue  # Si la fecha es incorrecta, volver a pedir datos

        if input("¿Quieres añadir otro amigo? (s/n): ").lower() != 's':
            break

    # Confirmar todos los cambios de una vez
    con.commit()

# Ingresar los amigos y mostrar la lista
ingresar_amigos()

# Consultar y mostrar los datos de la tabla 'amigos'
cur.execute("SELECT * FROM amigos")
print("\nLista de amigos:")
for amigo in cur.fetchall():
    print(amigo)

# Cerrar la conexión
con.close()

import sqlite3

# Crear una conexión a una base de datos en memoria
my_conn = sqlite3.connect(":memory:")  # BDA temporal

# Crear un cursor para ejecutar comandos SQL
my_cur = my_conn.cursor()

# Crear la tabla
my_cur.execute("CREATE TABLE TEST (id INTEGER, field1 TEXT, PRIMARY KEY(id))")

# Insertar algunos valores en la tabla
my_cur.execute("INSERT INTO TEST (id, field1) VALUES (1, 'Texto de prueba 1')")
my_cur.execute("INSERT INTO TEST (id, field1) VALUES (2, 'Texto de prueba 2')")
my_conn.commit()  # Confirmar los cambios

# Ejecutar una consulta para obtener los datos
my_cur.execute("SELECT * FROM TEST")

# Recuperar e imprimir los resultados
rows = my_cur.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
my_conn.close()
xx
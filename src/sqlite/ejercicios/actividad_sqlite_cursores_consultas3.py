
# vamos a ejecutar consultas mediante un cursor
import sqlite3

my_conn = sqlite3.connect("ejemplos.db")

my_cur = my_conn.cursor()

# no se usa commit() ya no se hacen cambios sobre la BDA
# usaremos execute() para ejecutar la consulta y fechone() / fetchall() para recuperar los resultados
my_cur.execute("select * from PERSONA")

# recuperamos todos los registros mediante el método fetchall()
# fetchall retorna lista de tuplas, donde cada tupla es un registro.
# Si la consulta no retorma ningún registro fetchall retorna una lista vacía []
registros = my_cur.fetchall() 
for reg in registros:
    print(reg)

my_conn.close()
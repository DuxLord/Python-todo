
# vamos a ejecutar concultas mediante un cursor

import sqlite3

my_conn = sqlite3.connect("ejemplos.db")

my_cur = my_conn.cursor()

# no se usa commit() ya no se hacen cambios sobre la BDA
# usaremos execute() para ejecutar la consulta y fechone() / fetchall() para recuperar los resultados
my_cur.execute("select * from PERSONA")

# recuperamos todos los registros mediante un bucle
reg = my_cur.fetchone() # primer registro
while reg != None:
    print(reg)
    reg = my_cur.fetchone() # siguiente registro

my_conn.close()
# vamos a ejecutar concultas mediante un cursor

import sqlite3

my_conn = sqlite3.connect("ejemplos.db")

my_cur = my_conn.cursor()

# no se usa commit() ya no se hacen cambios sobre la BDA
# usaremos execute() para ejecutar la consulta y fechone() / fetchall() para recuperar los resultados
my_cur.execute("select * from PERSONA")

# recuperamos el primer registro de la consulta
reg = my_cur.fetchone() # retorna tupla con los valores de las columnas o None si no hay nada que retornar
if reg == None:
    print("La consulta no ha devuelto ningún registro")
else:
    print(reg)

my_conn.close()
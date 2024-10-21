
# antes de ejecutar este programa hacemos un backup de ejemplos.db
import sqlite3

my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()

sentencia_sql = "drop table if exists AFILIACIONES"

my_cur.execute(sentencia_sql)

my_conn.commit()

my_conn.close()

# ahora entramos en sqlite3: .open ejemplos.db .tables y comprobamos que AFILIACIONES 
# se ha borrado. Salimos con .exit
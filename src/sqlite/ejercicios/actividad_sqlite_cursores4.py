
# antes de ejecutar este fichero restauramos la copia de ejemplos.db
import sqlite3

my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()

# sentencias
ins = '''insert into AFILIACIONES
    values(555555555, "1", "15/01/2020")'''
mod = '''update AFILIACIONES
    set persona = 333333333 where persona = 555555555'''
bor = '''delete from AFILIACIONES where persona = 333333333'''

# ejecución de sentencia
my_cur.execute(ins)
my_cur.execute(mod)
my_cur.execute(bor)

my_conn.commit() # solo un commit por transacción
my_conn.close()

import sqlite3

my_conn = sqlite3.connect(":memory:") # BDA temporal

# un cursor es un objeto que permite ejecutar intrucciones SQL en una BDA
my_cur = my_conn.cursor() # creamos cursor

# instrucciones de uso del cursor

# DDL
sentencia_sql = '''create table if not exists LENGUA_MATERNA(
    abreviatura TEXT,
    nombre TEXT,
    descripcion TEXT,
    PRIMARY KEY(abreviatura)
)''' 
my_cur.execute(sentencia_sql)

my_conn.commit() # hace permanentes los cambios en la BDA (transacción)

my_conn.close()
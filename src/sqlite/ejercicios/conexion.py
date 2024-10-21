import sqlite3

con = sqlite3.connect("test.db")
cur =con.cursor()

sentencia_sql = '''create table if not exists LENGUA_MATERNA(
abreviatura TEXT,
nombre TEXT,
descripcion TEXT,
PRIMARY KEY(abreviatura)
)'''
cur.execute(sentencia_sql) # ejecutamos SQL
con.commit()

con.close()
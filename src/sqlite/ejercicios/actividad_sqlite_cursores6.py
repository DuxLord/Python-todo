
import sqlite3

my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()

# técnica para insertar un grupo de registros con una sola instrucción
# usamos una lista de tuplas
lista = [(333333333, '1', '15/01/2020'),
         (333333333, '2', '02/01/2021'),
         (444444444, '3', '09/04/2021')]
ins = '''insert into AFILIACIONES
    values(?, ?, ?)'''

my_cur.executemany(ins, lista) # pasamos la lista de tuplas

my_conn.commit() # solo un commit por transacción
my_conn.close()

import sqlite3

my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()

# sentencias sql dinámico: utilizamos ? por cada parámetro de la sentencia
ins = '''insert into AFILIACIONES
    values(?, ?, "15/01/2020")'''
persona = 555555555
my_cur.execute(ins, (persona, "1")) # pasamos una tupla con los valores de los parámetros
                                    # si solo pasáramos un parámetro sería (persona,)
                                    #  y no (persona)

my_conn.commit() # solo un commit por transacción
my_conn.close()
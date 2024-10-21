import sqlite3
from datetime import date
def obtener_amigo():
    while True:
     nombre= input("Nombre de amig@: ")
     try:
         cad_fecha = input("Fecha de nacimiento (AAAA-MM-DD): ")
         ano, mes, dia = [int(x) for x in cad_fecha.split('-')]
         fecha_nac = date(ano, mes, dia)
         break
     except Exception as e:
         print(f'Se produjo un error tipo: {type(e)}')
         print('Vuelve a intentarlo')
    return (nombre, fecha_nac)
my_conn = sqlite3.connect("fechas.db")
amigo = obtener_amigo()
my_cur = my_conn.cursor()

sql = '''insert into amigos values (NULL, ?, ?)'''

my_cur.execute(sql, (amigo[0], str(amigo[1])))
my_conn.commit()

my_conn.close()
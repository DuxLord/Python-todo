import sqlite3

conn_sec = sqlite3.connect("secundaria.db")
conn_pri = sqlite3.connect("primaria.db")

# instruciones de uso de las BDA

conn_sec.close()
conn_pri.close()

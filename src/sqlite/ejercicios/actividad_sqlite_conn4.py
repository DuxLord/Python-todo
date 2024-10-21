
import sqlite3;

con_sec = sqlite3.connect("secundaria.db")
con_pri = sqlite3.connect("primaria.db")
con_inf = sqlite3.connect("infantil.db")

#Código que utiliza las BDA

con_sec.close()
con_pri.close()
con_inf.close()

import sqlite3

my_conn = sqlite3.connect("datos/ejemplos.db") # fichero que guarda la BDA
                                            # para BDA temporales ":memory:"


# código que utiliza la BDA

my_conn.close()

import sqlite3

my_conn = sqlite3.connect(":memory:") # para BDA temporales ":memory:"

# código que utiliza la BDA

my_conn.close()
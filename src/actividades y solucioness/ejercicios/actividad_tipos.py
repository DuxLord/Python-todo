"""
En Python todo son objetos.
Vamos a comprobar en el intérprete de Python a que clase pertenece cada tipo de datos.
Para ello, desde un terminal (de VSC por ejemplo) tecleamos python3 y ya estamos en el intérprete.
La función que debemos usar es type()

Probaremos los tipos que hay en las páginas 3 y 4.

Ejemplo:
natxo@natxo-TITAN:/media/natxo/KINGSTON/Acceso a datos/Introducción a Python$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> type(3)
<class 'int'>
>>> 

"""
# NÚMEROS
# int
print(f'type(3) -> {type(3)}')
print(f'type(-3) -> {type(-3)}')

# float
print(f'type(10.33) -> {type(10.33)}')
print(f'type(1.01E2) -> {type(1.01E2)}')

# complex
print(f'type(3.2+6j) -> {type(3.2+6j)}')
print(f'type(0.1+4.55j) -> {type(0.1+4.55j)}')

# BOOLEANOS
# bool
a = True
print(f'a = True, type(a) -> {type(a)}')
b = False
print(f'b = False, type(b) -> {type(b)}')

# SECUENCIAS
# str
print(f'type("Buenos días") -> {type("Buenos días")}')
print(f"type('Buenos días') -> {type('Buenos días')}")
print(f'type(\'Buenos días\') -> {type("Buenos días")}')

# list
print(f'type([1, "ya", True]) -> {type([1, "ya", True])}')
print(f'type([1, \'ya\', True]) -> {type([1, "ya", True])}')
print(f'type(["lunes", "jueves", "viernes", "domingo"]) -> {type(["lunes", "jueves", "viernes", "domingo"])}')

# tuple
print(f'type((1, "ya", True)) -> {type((1, "ya", True))}')
print(f'type((1, \'ya\', True)) -> {type((1, "ya", True))}')
print(f'type(("lunes", "jueves", "viernes", "domingo")) -> {type(("lunes", "jueves", "viernes", "domingo"))}')


# bytes
print(f'type(b"Pyhton is interesting") -> {type(b"Python is interesting")}')
print(f'type(b"\x00\x00\x00\x00\x00") -> {type(b"chr(92)x00chr(92)x00chr(92)x00chr(92)x00chr(92)x00")}') # f-string expression part cannot include a backslash

# bytearray
print(f'type(bytearray(b"Pyhton is interesting")) -> {type(bytearray(b"Python is interesting"))}')
print(f'type(bytearray(b"\x00\x00\x00\x00\x00")) -> {type(bytearray(b"chr(92)x00chr(92)x00chr(92)x00chr(92)x00chr(92)x00"))}')

# set
print(f'type({{3, 5, 1, 7, 4, 10}}) -> {type({3, 5, 1, 7, 4, 10})}')

# frozenset
print(f'type(frozenset({{3, 5, 1, 7, 4, 10}})) -> {type(frozenset({3, 5, 1, 7, 4, 10}))}')

# dict
print(f'type({{"one":1, "two": 2, "tree":3}}) -> {type({"one":1, "two":2, "tree": 3})}')

a = (1, "ya", True);print(a); a[0]= 2 ;print (a)
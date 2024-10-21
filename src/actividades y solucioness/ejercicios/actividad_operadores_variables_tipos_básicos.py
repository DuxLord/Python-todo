"""
Vamos a practicar un poco con los operadores de la página 4

Lo haremos en el entorno interactivo (intérprete)

"""

# Hay 35 palabras reservadas que NO se pueden usar para nombres de variables, objetos y clases:

# False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else,
# except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, 
# raise, return, try, while, with, yield

# Si se intenta asignar cualquier valor a una palabra reservada se eleva la excepción SyntaxError

"""
Podemos obtener la lista del intérprete:
>>> help ()
help> keywords

"""

# VARIABLES convenio snake_case (variables) SNAKE_CASE (constantes) pueden contener números 
# pero siempre empiezan por una letra

# el signo = se usa para asignar un valor a una variable. El tipo de la variable pasa a ser 
# el del dato asignado.

a = 5 # tipo entero
c = 'Hola mundo' # Tipo cadena
# print(f'Si una variable no está definida produce error {b}') # error
n_1 = 5
n_2 = 6
total = n_1 + n_2
print(total) # 11
print(f'{n_1} + {n_2} = {total}')

# NÚMEROS

num_int = 15 # int
num_real = 15.4 # float
num_cient = 0.1e-3 # float
num_complejo = 1.4 + 5.3j # complex

print(f'{num_int} es de tipo {type(num_int)}')
print(f'{int(num_real)} es de tipo {type(int(num_real))}') # int() pasa a entero
print(f'{num_real} es de tipo {type(num_real)}')
print(f'{float(num_int)} es de tipo {type(float(num_int))}') # float() pasa a real

suma = 3 + 2 # 5
print(suma)
cont = suma
cont += 1 # 6
print(cont)

# operadores a nivel de bits con enteros: 
# & (and), | (or), ^ (xor), ~ (not), << (desplazamiento a la izquierda), >> (desplazamiento a la derecha)

b1 = 47         # 0b0101111
b2 = 86         # 0b1010110
r = b1 | b2     # 0b1111111
print(f'{r} en binario {bin(r)}')

r = b1 ^ b2     # 0b1111001 
print(f'{r} en binario {bin(r)}')

r = b1 & b2     # 0b0000110
print(f'{r} en binario {bin(r)}')

r = b1 << 3     # 0b101111000
print(f'{r} en binario {bin(r)}')

r = b1 >> 3     # 000101
print(f'{r} en binario {bin(r)}')

r = ~b1         # 1110000 (sumo 1 y añado bit de signo)
print(f'{r} en binario {bin(r)}')

# Podemos probar estos en el intérprete y vemos que actúa como calculadora
print(16 / 3) # 5.333333333333333
print(12 / 4) # 3.0  La división siempre retorna float
print(16 // 3) # 5
print(16 % 3) # 1
print(5 * 4) # 20
print(5 ** 4) # 625
print(40 - 2 * 6) # 28 reglas de precendencia
suma = 3 + 2
suma += 1
print(suma) # 6
print(type(suma)) # int
print(float(suma)) # 6.0
print(type(suma)) # int
print(10 / 5e-3) # 2000.0


# BOOL

# El constructor es bool() y permite convertir cualquier objeto a un booleano

print(bool(True), bool(False))

# Serán False: las cosas vacías-> constantes None y False, números interpretados como 0, 
# objetos vacíos '', "", (), dict(), set(), range(0), []
print(bool(0), bool(0j), bool(''), bool(None), bool(set())) 
# Serán True: todo lo demás a no ser que se tenga un método mágico __bool__ que devuelva False 
# o __len__ que devuelva True
print(bool(1), bool(-1), bool('casa'), bool(24))

# or, and y not. Las operaciones and y not siempre devuelven uno de sus 
# operandos (aparte de su interpretación como True o False): 
#   and -> devueve el último
#   or -> devuelve el primero que cumple el cortocircuito lógico

print(24 and 89 and 2) # 2 
print(False and 21) # False (cortocircuito)
print(23 or 'casa') # 23
print(True and 0 and 90) # 0 (cortocircuito)

if 24 and 89 and 2:
    print("Se interpreta como True") # True
else:
    print("Se interpreta como False")

if 23 or 'casa':
    print("Se interpreta como True") # True
else:
    print("Se interpreta como False")

if True and 0 and 90:
    print("Se interpreta como True")
else:
    print("Se interpreta como False") # False

# cortocircuito lógico: propiedad que implementa Python para evaluar las expresiones de manera eficiente:
#   si evaluando and se encuentra un elemento False detiene la evaluación y devuelve ese valor
#   si evaluando or se encuentra un elmento True detiene la evaluación y devuelve ese valor

print(0 or 'libro' or 24 or x) # 'libro' en este caso no da error de sintaxis (NameError) por el cortocircuito
print(16 and True and 0 and x) # 0 y no da error de sintaxis por el cortocircuito

# COMPARACIONES >, >=, < , <=, ==, !=, is (objeto idéntico), is not (objeto no idéntico)
# la prioridad es idéntica para todas y es superior a los operadores booleanos

print(1 < 5 < 9 != 78 > 4) # True se pueden encadenar en ver de tener que usarlos por pares
print(1 < 5 and 5 < 9 and 9 != 78 and 78 > 4) # True

# operador == siempre está definido en el núcleo de Python. Los demás (<, <=, >, >=) cuando tienen sentido
# print(1 < 'pepito') # TypeError (no tiene sentido)

# el operador is (identidad) indica si 2 variables referencian al mismo objeto

a = 1; b = 1
print(a == b, a is b) # True True
c = [1]; d = [1]
print(c == d, c is d) # True False
c = d
print(c == d, c is d) # True True

# CADENA DE CARACTERES (STR)
cadena1 = "hola" # comillas dobles
cadena2 = 'hola' # comillas simples

cadena3 = 'doesn\'t'
cadena4 = "doesn't"
print(cadena3, cadena4) #  doesn't doesn't

# print() produce como salida la cadena que encierra entre paréntesis, omitiendo las comillas que la encierran
print('primera línea\nsegunda línea') # \n indica nueva línea

# una cadena raw debe interpretarse tal y como se escribe (se omiten los carácteres especiales que comienzan por \)
print(r'primera línea\nsegunda línea')

# triple comilla ('''''' o """""") si queremos que una cadena ocupe varias líneas
print("""primera línea
segunda línea""")
print("""    primera línea
    segunda línea""")

# las cadenas de caracteres se pueden concatenar (+) y repetir (*)
cadena = 'hola' + 'hola'
print (cadena)
cadena = 'hola' * 3
print(cadena)
print(cadena * 2)

# las cadenas son secuencias y, como tal, se gestionan:
# len(): devuelve la longitud de la cadena
print(len(cadena)) # 12
# se recorren mediante un índice que comienza por 0
print("abcde"[1]) # b
# el índice negativo -1 es el último elemento
print("abcde"[-1]) # e
# cualquier índice fuera de la cadena produce excepción: string index out of range
# se pueden usar intervalos o slices [i:j] donde i está incluido y j excluido
print("abcde"[1:3]) # bc
# el intervalo [:y] todos los caracteres hasta el y (excluido)
print("abcde"[:3]) # abc 
# el intervalo [x:] son todos los caracteres desde x al final
print("abcde"[3:]) # de

# las cadenas son ÍNMUTABLES: no se pueden reescribir. Hay que renombrar.
# Toda operación de cadenas crea otra nueva como resultado.
cadena = "inmutable"
# cadena[0] = "1" # TypeError
cadena = "1" + cadena[1:]
print(cadena) # 1nmutable
# str() convierte a cadena
cadena = str(3) + str(3)
print(cadena) # 33

# algunos métodos específicos de las cadenas de caracteres

print("abcde".upper()) # ABCDE
print("ABCDE".lower()) # abcde
print("Juanito".swapcase()) # jUANITO
print("abcde".find("cd")) # 2
print("ababcde".count("ab")) # 2
print("abcde".replace('a', 'x')) # xbcde
print(" abcde ".strip()) # abcde

# averigua los resultados
cad_e = " esta cadena es muy larga "
print(len(cad_e)) # 26

cad = cad_e.strip()
print(len(cad)) # 24
print(cad.find("muy")) # 15
CAD = cad.upper()
cad = CAD.lower()
print(CAD, cad)
print(type(cad))
print(cad[4]) # " "
print(cad[-4]) # a
print(cad[1:3]) # st
print(cad[:3]) # est
print(cad[3:]) # a cadena es muy larga
print(cad + CAD)


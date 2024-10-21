# LISTA tipo de datos secuencia mutable que permite almacenar elementos de cualquier tipo

# crear una lista -> [e1,e2,e3 ...]
numeros = [1, 2, 3, 4, 5]
print(numeros)

vocales = ['a', 'e', 'i', 'o', 'u'] 
print(vocales)

# crear una lista mediante el constructor list()
otro = list(numeros) # crea nueva lista
print(otro)
print(id(otro), id(numeros)) # id del objeto: donde se encuentra en memoria. En este caso son distintos

vocales = list ("aeiou")
print(vocales)

# ojo con esto
lista1 = [10, 20, 30]
lista2 = lista1 # misma lista con diferente nombre
print(id(lista1), id(lista2)) # son el mismo objeto
lista1[0] = 10000
print(lista1, lista2)

# OPERACIONEWS CON LISTAS
# Acceso a elementos: operador []
colores = ['rojo', 'verde', 'azul', 'rojo', 'azul']
colores[0] = 'negro'
print(colores)
print(colores[1])

# recorrido de listas
for color in colores:
    print(color, end=' ')


for i in range(len(numeros)):
    numeros[i] *= 10
print()
print(numeros)

# longitud de la lista: len()
print(len(numeros), len(colores))

# sublistas nombre_lista[inicio:fin:salto] recuerda que se incluye hasta fin - 1
num = [1, 2, 3, 4, 5]
print(num[2], num[4], num[-2])
pares = num[1:5:2]
print(pares)
impares = num[0:5:2]
print(impares)
copia = num[::] # similar a ::1
print(copia)
print(id(num), id(copia)) # son diferentees
copia_inversa = num[::-1] # copia superficial (solo un nivel)
print(copia_inversa)

# ojo 
pares[0] = 10
print(pares[0], num[0]) # como vemos no hay peligro ya que tienen ids diferentes

# añadir elementos con append()
numeros = [5, 2, 3, 4, 1]
numeros.append(8); print(numeros)
numeros.append([7, 9]); print(numeros) # una lista puede ser elemento de una lista

# concatenando listas con +
numeros = [5, 2, 3, 4, 1]
numeros = numeros + [8]; print(numeros) # se añade al final
numeros = [6, 7] + numeros; print(numeros) # se añade al principio

# borrar elementos con pop() que borra el último (por defecto)
numeros = [5, 2, 3, 4, 1]
num = numeros.pop(); print(numeros, num)
num = numeros.pop(0); print(numeros, num)

# Hemos visto str y list pero no todo
# Para examinar que tiene cada clase podemos poner en el intérprete dir(str) o dir(list)
# con help(str) o help(list) tendremos información más detallada
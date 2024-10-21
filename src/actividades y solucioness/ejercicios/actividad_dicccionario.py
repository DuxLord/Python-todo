# DICCIONARIO tipo de dato compuesto por pares clave:valor
# clave puede ser cualquieer tipo inmutable (texto o numeros)
# valor puede ser cualquier tipo de datos
# los elementos de un diccionario no guardan ningún orden (a diferencia de las listas)

# crear diccionario
dic = {'nombre': "Mafalda", 'ama': "Los Beatles", 'odia': "sopa"} # con el operador {} 
print(dic)

# con el constructor dict() pasándole los pares clave:valor
dic = dict(nombre="Mafalda", ama="Los Beatles", odia="sopa")
print(dic)

# creando un diccionario vacío y con el operador asignación para los pare clave:valor
dic = {}
dic["nombre"] = "Mafalda"
dic["ama"] = "Los Beatles"
dic["odia"] = "sopa"
print(dic)

# operaciones
print(len(dic)) # longitud len()

# obtener la lista de elementos items()
print(dic.items())

# obtener la lista de claves keys()
print(dic.keys())

# obtener la lista de valores values()
print(dic.values())

# recorrer un diccionario
for k in dic.keys(): # recorremos las keys
    print(k, end=' ')
print()

for k, v in dic.items(): # recorremos keys y values
    print(k,'-->',v)

# borrar elementos con el método pop(clave[, valor_defecto])
valor = dic.pop('nombre')
print(dic, valor)

valor = dic.pop('nombre', 'No existe')
print(dic, valor)

# podemos obtener más info sobre dict con dir(dict) y help(dict) en el intérprete de python3


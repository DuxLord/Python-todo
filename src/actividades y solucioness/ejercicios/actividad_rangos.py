# Los rangos son secuencias de enteros inmutables
# Se crean con el constructor range()
# range(final) genera enteros desde 0 hasta final-1
# ojo en estos primeros ejemplos se genera una lista a partir de un rango
print(list(range(5)))  # [0, 1, 2, 3, 4]

# range(inicio, final) genera enteros de inicio a final-1
print(list(range(3, 6))) # [3, 4, 5]
print(list(range(-3, 0))) # [-3, -2, -1]
print(list(range(4, 4))) # []

# range(inicio , final, paso) comenzamos por inicio y el número siguiente es número+paso
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]

# los rangos son iteradores: cuando se crean no guardan la información que representan
# sino el procedimiento necesario para generar la secuencia de números.
# Por esto, ocupan muy poco espacio de memoria. Se generan los valores de uno en uno y no todos a la vez.

rango = range(0, 24, 2)
print(rango) # range(0, 24, 2)

print(8 in rango, 7 in rango) # True False
print(rango[3]) # 6
print(rango[7]) # 14
print(rango[-2]) # 20
print(rango[:4]) # subrango range(0, 8, 2)
print(list(rango[:4])) # [0, 2, 4, 6]
print(rango[3:]) # subrango range(6, 24, 2)
print(list(rango[3:])) # [6, 8, 10, 12, 14, 16, 18, 20, 22]



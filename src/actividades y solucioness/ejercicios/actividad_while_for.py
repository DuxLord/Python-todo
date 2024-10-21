# while para validar dato introducido por teclado
opcion = input("¿Quieres seguir? (S/N): ")

while opcion.upper() != 'S' and opcion.upper() != 'N':
    opcion = input("¿Quieres seguir? (S/N): ")

print("Opción correcta: ", opcion)

# iterando sobre una secuencia
palabra = "HOLA"
for i in range(len(palabra)):
    print(i, '-->', palabra[i])

# break, dentro de un bucle, provoca la finalización del mismo
# continue finaliza la iteración actual y pasa a la siguiente

# contar números de una lista
lista = [1, "Pepe", 2, "Pedro", 3, "Paula"]

i = 0; cont = 0
while i < len(lista):
    if isinstance(lista[i], int):
        cont += 1
    i += 1
        

print(f"Hay {cont} enteros")

# pass es una sentencia vacía (no hace nada). Es un "lo codifico más adelante" para evitar errores de sintaxis.
# while True: # ojo bucle infinito (ctrl + c)
#    pass

for i in range(len(palabra)):
    pass

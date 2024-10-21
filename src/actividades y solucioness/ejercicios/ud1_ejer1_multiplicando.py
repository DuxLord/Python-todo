###################################
# UNIDAD 1 - Ejercicio 1          #
# Tabla de multiplicar (SOLUCIÓN) #
###################################

print()
numero = int(input("Dame un número entero del 1 al 10: "))
print()

if (numero >= 1 and numero <= 10):
    print("TABLA DE MULTIPLICAR DEL Nº", numero, ":")
    for i in range(1, 11):
        print("{0:2} * {1:2} = {2:3}".format(i, numero, i*numero))
else:
    print("Error de introducción de datos.")

input()
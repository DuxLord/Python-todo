# las funciones tienen un nombre camel_case
# calculadora con dos parámetros de entrada y devuelve 
# cuatro resultados de operaciones
def calculadora(a, b):
    '''realiza operaciones básicas.'''
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b

    return (suma, resta, producto, division) # tupla

a = int(input("Dame el operando 1: "))
b = int(input("Dame el operando 2: "))
resultado = calculadora(a, b)

for i in range(len(resultado)):
    print("resultado", i , "-->", resultado[i])
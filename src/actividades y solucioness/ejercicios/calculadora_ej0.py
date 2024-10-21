def calcular(a, b):
    sumar = a + b
    restar = a - b
    multiplicar = a * b
    dividir = a / b

    return f"suma = {sumar}, resta = {restar}, multiplicación = {multiplicar}, división = {dividir}"

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
print(calcular(a, b))


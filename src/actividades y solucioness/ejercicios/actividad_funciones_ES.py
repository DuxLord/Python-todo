# input() función que espera una cadena por teclado y se pulse intro.
texto = input("Escribe una frase, por favor: ")
print(texto)

# si necesitamos leer del teclado algo diferente a una cadena haemos la conversión int(), float, ...
entero = int(input("Dame un número entero: "))
print(entero)

real = float(input("Dame un número real: "))
print(real)

# print() permite mostrar información por pantalla. Es muy versátil:

print("Hola %s." % ("Pepito")) # operador %

print("%s, trae %d tebeos de %.2f€ cada uno." % ("Pepito", 5, 12.5)) 

print("{} trae {} tebeos de {:.2f}€ cada uno.".format("Pepito", 5, 12.5)) # con {} + format

nom = "Pepito"; num = 5; preu = 12.5
print(f'{nom} trae {num} tebeos de {preu}€ cada uno.') # con f-string
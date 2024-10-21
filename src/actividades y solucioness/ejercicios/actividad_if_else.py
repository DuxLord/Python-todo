seguir = input( "¿Quieres seguir (S/N)? ")
if seguir == 'S':
    print("Has elegido seguir")
else:
    print("Has elegido no seguir")

num = int(input("Dame un número (1-10): "))
if num < 5:
    print("Sigue intentándolo.")
else:
    print("¡Enhorabuena!")

num = int(input("Dame un número (1-10): "))
if num <= 2:
    print("Muy deficiente")
elif 3 <= num <= 4:
    print("Insuficiente")
elif num == 5:
    print("Aprobado")
elif num == 6:
    print("Bien")
elif 7 <= num <= 8:
    print("Notable")
elif num >= 9:
    print("Sobresaliente") 
from sre_constants import error


def valida_opcion():
    '''

    funcion para validar
    :return: boolean
    '''
    while True:
        print('''===========================
  GAMIFICACIÓN EN EL AULA
===========================
 1 - A
 2 - A
 3 - A
 4 - A
 5 - A
 0 - Salir
---------------------------''')

        a = int(input("Dame una opción:"))
if a == 0:
            print("Saliendo...")
            break
        if a <= 5 and a >= 1:
            print("Gracias por la seleccióon")

        else:
            print(error)



valida_opcion()
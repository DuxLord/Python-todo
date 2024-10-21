# es posible lanzar excepciones de forma intencionada por el programador
def elevando_excepciones():
    while True:
        valor = int(input('Introduce un número entero positivo: '))
        if valor < 0:
            raise ValueError(f'El número introducido {valor} no es positivo')
        else:
            print(valor)
            break

elevando_excepciones()

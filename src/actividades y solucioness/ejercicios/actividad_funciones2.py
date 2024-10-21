def menor_valor(iter):
    '''se le pasa un objeto que sea compatible con la función min (iterable)'''
    return min(iter)

def iniciales(cadena, sep=' '):
    '''devuele las iniciales de cada palabra en la cadena separadas por sep. 
    sep por defecto es ' '. Funciona si el objeto que se le pasa tiene la función split.  '''
    return ''.join(x[0].upper() for x in cadena.split(sep)) # el parámetro de join es una expresión generadora (más adelante)

def iniciales2(cadena, sep=' '):
    '''versión más simplista sin la expresión generadora'''
    resultado = ''
    lista_palabras = cadena.split(sep)
    for x in lista_palabras:
        resultado += x[0].upper()
    return resultado

if __name__ == '__main__':
    # testeo menor_valor
    print(menor_valor([1, 2, 3, 4])) # 1
    print(menor_valor(range(4))) # 0
    print(menor_valor(['Juan', 'Pedro', 'Ana'])) # Ana

    # testeo de iniciales
    print(iniciales('Juan Pérez Martínez'))
    print(iniciales('en un lugar de la Mancha de cuyo nombre no quiero acordarme'))
    print(iniciales('el,arbol,del,parque', sep=','))

    print(iniciales2("Pepito come pipas"))
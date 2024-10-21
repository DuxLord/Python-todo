# utilizando el traceback o traza de error averigua el fallo de este programa
# el traceback nos aparece cuando termina un programa por una excepción no manejada

def capitalizar(elem):
    return elem.capitalize()


def formatea(elem):
    limpio = elem.strip()
    capitalizado = capitalizar(limpio)
    return capitalizado


def formateador(elementos):
    resultado = []
    for elem in elementos:
        resultado.append(formatea(elem))
    return resultado


if __name__ == '__main__':
    print(formateador('   Jose   '))
    print(formateador([' pepito ', ' juanita ']))

# cuando lo tengas claro haz las correcciones oportunas

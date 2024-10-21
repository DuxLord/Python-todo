import os
import random
import re
import sys
from re import match

# Constantes
rueda_cifrado = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('''
 ██████ ██ ███████ ██████   █████  ██████   ██████       ██████ ███████ ███████  █████  ██████  
██      ██ ██      ██   ██ ██   ██ ██   ██ ██    ██     ██      ██      ██      ██   ██ ██   ██ 
██      ██ █████   ██████  ███████ ██   ██ ██    ██     ██      █████   ███████ ███████ ██████  
██      ██ ██      ██   ██ ██   ██ ██   ██ ██    ██     ██      ██           ██ ██   ██ ██   ██ 
 ██████ ██ ██      ██   ██ ██   ██ ██████   ██████       ██████ ███████ ███████ ██   ██ ██   ██''')

def limpiarTexto(texto):
    return (texto
            .replace('ñ', 'nn')
            .replace('á', 'a')
            .replace('é', 'e')
            .replace('í', 'i')
            .replace('ó', 'o')
            .replace('ö','o')
            .replace('ú', 'u')
            .replace('ü', 'u')
            .replace('\n', ' ')
            .replace('\r', ' ')
            .upper())



def procesar(dicc):
    """Lee el fichero del diccionario y lo procesa: sin tildes ni diéresis, mayúsculas
    y Ñ -> NN. Retorna un set sin \n o \r\n al final de cada elemento.

    :param dicc: str Nombre del fichero que contiene palabras en castellano
    :returns: list Lista de palabras procesada. Lista vacia en caso de error
    """
    try:
        # La librería en Linux falla si no se hace así ...
        if os.name == 'posix':  # Linux, MacOS
            d = open(dicc, 'r', encoding='latin-1')
        else:                   # Windows
            d = open(dicc,'r', encoding='latin-1')

        todo = d.read()

        '''###########################'''
        '''RELLENA EL CÓDIGO QUE FALTA'''
        '''###########################'''

        todo = limpiarTexto(todo)

        d.close()

        miset = set(todo.split(' '))

        return miset

    except FileNotFoundError:
        print('Fichero "{0}" no encontrado.\nPor favor, escriba correctamente el nombre del fichero y/o la ruta'.format(dicc))
        return []
    except:
        print("Error inesperado: {0}".format(sys.exc_info()[0]))
        return []



def max_palabra(set_palabras):
    """
    Retorna el tamaño máximo de palabra en el set de palabras en castellano

    :param set_palabras: set(str) set de palabras en castellano
    :returns:
    int Tamaño máximo encontrado
    """

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''
    mayor = 0

    for palabra in set_palabras:
        if len(palabra) > mayor:
            mayor = len(palabra)

    return mayor



def num_coincidencias(set_palabras, texto_candidato, min_sub, max_sub):
    """
    Compara el todas las posibles subcadenas de texto_candidato entre los tamaños
    min_sub y max_sub contra el set de palabras

    :param set_palabras: list todas las palabras del castellano
    :param texto_candidato: str Texto en el que se buscan coincidencias dentro de la lista
    :param min_sub: int Tamaño mínimo de subcadena a buscar
    :param max_sub: int Tamaño máximo de subcadena a buscar

    :returns:
    int Número de coincidencias en el diccionario
    """

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    coincidencias = 0

    for palabra in set_palabras:
        for palabra_texto in texto_candidato.split():
            if min_sub >= palabra_texto <= max_sub:
                if match(palabra_texto, palabra):
                    coincidencias += 1

    return coincidencias



def texto_plano(fichero_texto_plano:str):
    """Pide al ususario que escriba un texto y se guarda en un fichero. Se pide línea a línea
    y ,para acabar, pulsamos INTRO y luego CTRL + D

    :param fichero_texto_plano: str nombre del fichero donde se guarda el texto plano
    """

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    with open(fichero_texto_plano, 'w', encoding='latin-1') as file:
        print("Escribe el texto. Para finalizar, pulsa ENTER sin escribir nada:")

        while True:
            linea = input()
            piezas = linea.split(" ")
            if not linea:
                break
            file.write(linea + '\n')

    print(f"Texto guardado en {fichero_texto_plano}")



def cifrar(fichero_texto_plano, fichero_cifrado_cesar):
    '''
    Dado un fichero de texto en plano y una clave aplica el cifrado César según los
    requerimientos: eliminar espacios y signos de puntuación,
    vocal con tildes -> sin tildes, min -> MAY, Ñ -> NN, texto cifrado 5 en 5
    comenzando por la izquierda.
    ASUMO que los números se quedan igual y caracteres tipo: ¡!¿? también
    La clave utilizada será aleatoria de 1 a 25.

    :param fichero_texto_plano: str nombre de fichero con el Texto a cifrar.
    Se procesa para cumplir requisitos
    :param fichero_cifrado_cesar: str nombre de fichero donde se guardan el texto cifrado

    :returns:
    str | None Texto cifrado para la clave aleatoria o None si hubo algún error

    '''

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    print("CIFRAR")

    try:
        with open(fichero_texto_plano, 'r', encoding='latin-1') as f:
            contenido = f.read()
            print("Fichero plano leido correctamente")
            contenido = limpiarTexto(contenido)
            contenido = contenido.replace(" ", "")
            print(contenido)

            contenido_formateado = ""
            contador = 0
            for letras in contenido:
                contenido_formateado+=letras
                contador += 1
                if contador == 5:
                    contenido_formateado += " "
                    contador = 0

            print(contenido_formateado)


    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_texto_plano}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_texto_plano}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    try:
        with open(fichero_cifrado_cesar, 'w', encoding="latin-1") as file:
            print("Fichero de cifrado abierto correctamente")
            contenido_fichero_cifrado = ""
            clave = random.randint(1,25)

            for caracter in contenido_formateado:
                if caracter in "¿?¡! 1234567890":
                    contenido_fichero_cifrado += caracter
                else:
                    index = rueda_cifrado.index(caracter)
                    index = index + clave
                    if index > 25:
                        index -= 26
                    elif index < 0:
                        index += 26

                    contenido_fichero_cifrado += rueda_cifrado[index]

            file.write(contenido_fichero_cifrado)

    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None



def descifra(fichero_cifrado_cesar, fichero_texto_plano_candidato, clave):
    '''
    Dado un texto cifrado (del fichero_cifrado_cesar) y una clave realiza un
    desplazamiento en sentido contrario a dicha clave. El resultado se guarda en
    fichero_texto_plano_candidato y se pone como sufijo la clave empleada

    :param fichero_cifrado_cesar: str nombre del fichero con el texto a descifrar
    :param fichero_texto_plano_candidato: str nombre del fichero con el texto tras
    aplicar la clave en sentido contrario para descifrar
    :param clave: int clave a aplicar. De 1 a 25

    :returns: str | None texto descifrado o None si hubo algún error
    '''

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    print("DESCIFRAR")

    try:
        with open(fichero_cifrado_cesar, 'r', encoding="latin-1") as file:
            contenido_fichero_cifrado = file.read()
            print("Fichero cifrado leido correctamente")
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    try:
        with open(fichero_texto_plano_candidato, 'w', encoding="latin-1") as file:
            descifrado = descifras(contenido_fichero_cifrado, clave)
            file.write(descifrado)
            print("Fichero descifrado escrito correctamente")
            return descifrado
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None



def descifras(texto_cifrado, clave):
    '''
    Dado un texto cifrado realiza un desplazamiento en sentido contrario de la rueda según la clave

    :param texto_cifrado: str Cadena con el texto cifrado
    :param clave: int Valor de la clave (1 a 25)

    :returns:
    str Texto descifrado
    '''

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    contenido_descifrado = ""

    clave = clave * -1

    for caracter in texto_cifrado:
        if caracter in "¿?¡! 1234567890":
            contenido_descifrado += caracter
        else:
            index = rueda_cifrado.index(caracter)
            index = index + clave
            if index > 25:
                index -= 26
            elif index < 0:
                index += 26

            contenido_descifrado += rueda_cifrado[index]

    return contenido_descifrado



def descifrar_fuerza_bruta(fichero_cifrado_cesar, fichero_resultados):
    '''
    Abre el fichero con el texto cifrado y saca los textos correspondientes
    a intentos de descifrar con las claves de 0 a 26 (en realidad solo hace falta
    de 1 a 25).

    :param fichero_cifrado_cesar: str Fichero con el texto cifrado
    :param fichero_resultados: str se generan 25 ficheros como resultado de aplicar todas las claves.
    La clave aplicada aparece como sufijo en el nombre del fichero

    :returns:
    stdout Todos los textos precedidos de la clave aplicada en cada caso.
    '''

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''

    print("DESCIFRAR BRUTA")

    try:
        with open(fichero_cifrado_cesar, 'r', encoding="latin-1") as file:
            contenido_fichero_cifrado = file.read()
            print("Fichero cifrado leido correctamente")
            file.close()
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    try:

        if not os.path.exists("resultado"):
            os.makedirs('resultado')

        descifrado = ""
        archivo = ""
        for i in range(1,26):
            archivo = f"resultado/{fichero_resultados}_clave{i}"
            with open(archivo, 'w', encoding="latin-1") as file:
                descifrado_unilateral = descifras(contenido_fichero_cifrado, i)
                descifrado += descifrado_unilateral + "\n"
                file.write(descifrado_unilateral)
                file.close()
            print(f"{i}. " + descifrado_unilateral)
        return descifrado
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{archivo}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None



def descifrar_fuerza_bruta_dic(fichero_cifrado_cesar, fichero_resultado, diccionario:list , porcentaje=0.25, rapido=False, minPalabra=None, maxPalabra=None):
    '''
    Abre el fichero con el texto cifrado y saca los textos correspondientes
    a intentos de descifrar con las claves de 0 a 26 (en realidad solo hace falta
    de 1 a 25). Por cada texto, indica el número de subcadenas que coinciden con
    entradas del diccionario

    :param fichero_cifrado_cesar: str Fichero con el texto cifrado
    :param fichero_resultado: str Fichero con los resultados (texto y coincidencias) de aplicar todas las claves
    :param diccionario: list lista de palabras en castellano
    :param porcentaje: int Aquellas claves que generen un porcentaje (en tanto por 1) de coincidencias cercano a
    la mejor (porcentaje 1) tal que 1 - porcentaje <= coincidencias <= 1 serán consideradas como solución
    alternativa
    :param rapido: boolean Si es False mira todas las posibles subcadenas. Si es True pide la longitud mínima y
    máxima de las cadenas a considerar. De esta forma, si se hace con criterio, se acelera bastante la búsqueda
    en el diccionario
    :param minPalabra: int Tamaño mínimo de palabra a considerar
    :param maxPalabra: int Tamaño máximo de palabra a considerar

    :returns:
    stdout Todos los textos precedidos de la clave aplicada en cada caso. Como
    side-effect crea un fichero con los resultados. Si hay algún tipo de error
    informa de ello
    '''

    '''###########################'''
    '''RELLENA EL CÓDIGO QUE FALTA'''
    '''###########################'''





def menu():
    '''Muestra un menú por pantalla

    :returns:
    int opción escojida
    '''
    print('\n*** Hackeando, a lo bruto, a Julio César ***')
    print('1) Crear fichero en texto plano')
    print('2) Cifrar fichero')
    print('3) Fuerza bruta y resolución a "ojo"')
    print('4) Fuerza bruta y resolución por diccionario')
    print('5) Salir')
    opcion = input('Escoge opción: ')

    # validación
    modelo = re.compile(r'[12345]')
    while modelo.fullmatch(opcion) == None:
        opcion = input('Escoge opción (entre 1 y 5): ')

    return int(opcion)


def esFlotanteAdecuado(porcentaje):
    '''
    Comprueba si es un float adecuado: 0.0 <= porcentaje <= 1.0

    :returns:
    bool
    '''
    try:
        porcentaje = float(porcentaje)
        if 0.0 <= porcentaje <= 1.0:
            return True
        else:
            return False
    except:
        return False



def esIntAdecuado(numero, minimo, maximo):
    '''
    Comprueba si es un int adecuado: minimo <= numero <= maximo

    :returns:
    bool
    '''
    try:
        numero = int(numero)
        if minimo <= numero <= maximo:
            return True
        else:
            return False
    except:
        return False



if __name__ == "__main__":

    set_palabras_castellano = procesar("Diccionario.txt")
    print("PROCESAR REALIZADO CORRECTAMENTE \n\n\n")

    texto_plano('test.txt')
    print("TEXTO PLANO REALIZADO CORRECTAMENTE \n\n\n")

    texto_cifrado = cifrar('test.txt', 'test_cifrado.txt')
    print("CIFRAR REALIZADO CORRECTAMENTE \n\n\n")

    texto_descifrado = descifra('test_cifrado.txt', 'test_candidato.txt', 10)
    print("DESCIFRA REALIZADO CORRECTAMENTE \n\n\n")

    descifrar_fuerza_bruta('test_cifrado.txt', 'test_resultado.txt')
    print("DESCIFRAR FUERZA BRUTA REALIZADO CORRECTAMENTE \n\n\n")
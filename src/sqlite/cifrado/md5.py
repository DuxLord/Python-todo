import hashlib


def extraer_identificadores(cadena_original, sep=' '):
    return cadena_original.split(sep)

def aplicar_hash(lst):
    md5s = []
    for cad in lst:
        m = hashlib.md5(cad.encode('utf-8'))
        md5s.append(m.hexdigest())
    return md5s

def escribir_a_fichero(data, nombre_fichero='out.txt'):
    with open(nombre_fichero, 'w') as f:
        for d in data:
            f.write(d + '\n')
    return nombre_fichero

cadena_original = 'Hola mundo miaur'
identificadores = extraer_identificadores(cadena_original, sep='<>')
id_modificados = aplicar_hash(identificadores)
nombre_fichero = escribir_a_fichero(id_modificados)
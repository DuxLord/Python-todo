# Las excepciones se pueden definir basándose en una clase de excepción definida
# en la librería estándar o en una propia.
# Las excepciones tienen una jerarquía que comienza con BaseException. Todas las demás
# excepciones heredan de dicha clase. Los casos de error se van haciendo cada vez más 
# específicos.
# vamos a crear excepciónes más específicas que IndexError:
# TupleIndexError: índice no encontrado en tupla
# ListIndexError: índice no encontrado en lista

# Para más info de excepciones python3 -> help() -> topics -> EXCEPTIONS
# https://docs.python.org/es/3.10/library/exceptions.html


import sys

class TupleIndexError(IndexError):
    pass

class ListIndexError(IndexError):
    pass

def get_index_value(obj, index):
    try:
        return obj[index]
    except IndexError as e:
        args, description, tb = sys.exc_info()
        if isinstance(obj, tuple):
            raise TupleIndexError(description).with_traceback(tb)
        elif isinstance(obj, list):
            raise ListIndexError(description).with_traceback(tb)
        else:
            raise e
        
# get_index_value((1, 2, 3), 4)
get_index_value([1, 2, 3], 4)
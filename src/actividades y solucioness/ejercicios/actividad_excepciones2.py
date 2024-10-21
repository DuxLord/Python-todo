def busca_elemento(obj, indice_o_clave):
    '''busca un elemento en una secuencia'''
    try:
        return obj[indice_o_clave]
    except IndexError:
        print(f'Índice "{indice_o_clave}" utilizado no accesible')
    except KeyError:
        print(f'Clave "{indice_o_clave}" utilizada no encontrada')
    except Exception as e:
        print(f'Excepción inesperada "{e}"')
        return -1
    
obj  = [1, 2, 3]
print(busca_elemento(obj, 1))

busca_elemento(obj, 100)
obj = dict(color='Verde', tipo='Coche')
print(busca_elemento(obj, 'color'))

busca_elemento(obj, 'modelo')

busca_elemento(obj, str.upper)

obj = set([1, 2, 3])
busca_elemento(obj, 'pepe')
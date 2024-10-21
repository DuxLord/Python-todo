# módulo ejemplo
def resta(op1, sust):
    return op1 - sust

def suma(op1, op2):
    return op1 + op2

# los módulos pueden ser ejecutables: para testeo
# este bloque no se ve al importar
if __name__ == '__main__':
    print(resta(1, 2))
    print(suma(1, 2))
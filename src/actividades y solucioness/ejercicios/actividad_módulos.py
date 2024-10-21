# un módulo es un fichero de texto plano con extensión .py (snake_case.py)
# para importar un módulo usamos import seguido del nombre del módulo y de la jeraquía de paquetes  a la que pertenezca
# import nombre_módulo
# import nombre_paquete.nombre_módulo
# import paquete.subpaquete.nombre_módulo

# puede que nos interese importar algunos elementos (funciones, clases) de un módulo: usaremos from ... import ...
# from nombre_módulo import elemento
# from nombre_módulo_import elemento1, elemento2, elemento3, ... elementoN

# Ahora podemos usar el elemento correspondiente sin necesidad de anteponer el namespace correspondiente.
from aritmetico import resta
print(resta(10, 5.5)) # 4.5

import aritmetico # aquí tocará usar el namespace para suma()
print(aritmetico.suma(10, 5.5)) # 15.5
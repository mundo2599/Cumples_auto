from creador import Creador
from excel import Excel
from datetime import datetime

excel = Excel()
maker = Creador()

print('Inicio')
inicio = (int(input('Mes: ')), int(input('Dia: ')))
print('Fin')
fin = (int(input('Mes: ')), int(input('Dia: ')))

personas = excel.get_names(inicio, fin)
for x in personas:
    nombre = x['nombre']
    if '.' in nombre:
        print('Nombre original: ' + nombre)
        text = input('Nombre en foto (o enter): ')
        if text != '':
            nombre = text

    # split si mayor a len
    nombre = nombre.lower()
    maker.create(nombre, x['numero'], x['fecha'])
    print('Creado: ' + nombre)

# TODO: Archivo de excel con enlace
# TODO: Primer letra de nombre mayuscula
# TODO: Espacio final en algunas imagenes
from creador import Creador
from excel import Excel
from datetime import date


print('Inicio')
inicio = date(1, int(input('Mes: ')), int(input('Dia: ')))
print('Fin')
fin = date(1, int(input('Mes: ')), int(input('Dia: ')))
excel = Excel(inicio, fin)

maker = Creador()
personas = excel.get_names()

# Crear fotos
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

# Crear csv
excel.crear_csv()

# TODO: Archivo de excel con enlace
# TODO: Primer letra de nombre mayuscula
# TODO: Espacio final en algunas imagenes
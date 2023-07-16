from ManejoArchivos import ManejoRecursos

# Sin try catch
with open( 'prueba.txt', 'r', encoding='utf8' ) as archivo:
    print(archivo.read())

# Simulando el with open de arriba con clases
with ManejoRecursos('prueba.txt') as archivo2:
    print(archivo2.read())
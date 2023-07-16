
try:
    archivo = open('prueba.txt','r', encoding='utf8')
    # leer todo
    #print(archivo.read())

    # leer un pedazo
    #print(archivo.read(3))

    # leer lineas completas
    #print(archivo.readline())

    # Iteracion de linea
    # for linea in archivo:
    #     print(linea)

    #print(archivo.readlines()[-1])
    ultimaLinea: list = archivo.readlines()
    for line in ultimaLinea:
        print( line )
except Exception as ex:
    print(ex)
finally:
    archivo.close()
    print('Flujo Cerrado')
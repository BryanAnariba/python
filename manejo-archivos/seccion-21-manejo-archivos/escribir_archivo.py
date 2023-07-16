# open( nombreArchivo, w=escritura|r=lectura, charset )
try:   
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('hello')
    archivo.write('\nAdios')
except Exception as ex:
    print(ex)
finally:
    archivo.close()
    print('Flujo del archivo cerrado')

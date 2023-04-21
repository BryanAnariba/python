conceptosPorgramacion: dict = {
    'IDE': 'Entorno de Desarrollo Integrado',
    'OOP': 'Programacion Orientada a Objetos',
    'DBMS': 'Gestor de Manejo de Base de Datos'
}

print( conceptosPorgramacion )
print( f'Tamanio: { len( conceptosPorgramacion ) }' )
print( f'Elemento OOP: { conceptosPorgramacion["OOP"] }' )
print( f'Elemento OOP: { conceptosPorgramacion.get( "OOP" ) }' )

conceptosPorgramacion['DBMS'] = 'sistema de administración de bases de datos'
print( f'Corrigiendo el contenido del elemento DBMS: { conceptosPorgramacion.get( "DBMS" ) }' )

# Recorrer elementos de un diccionario
print( '\nIMPRIMIENDO DICCIONARIO' )
for concepto in conceptosPorgramacion:
    print( f'{concepto}' )

print( '\nIMPRIMIENDO LLAVE Y VALOR' )
for concepto, valor in conceptosPorgramacion.items():
    print( f'{ concepto } - { valor }' )

print( '\nIMPRIMIENDO SOLO LLAVES' )
for concepto in conceptosPorgramacion.keys():
    print( concepto )

print( '\nIMPRIMIENDO SOLO VALORES' )
for valor in conceptosPorgramacion.values():
    print( valor )

print( '\nVERIFICAR SI IDE EXISTE EN EL DICCIONARIO' )
existeIDEenDict: bool = 'IDE' in conceptosPorgramacion
print( f'Existe: { existeIDEenDict }' )

print( '\nAGREGANDO AL DICCIONARIO' )
conceptosPorgramacion['PK'] = 'PRIMARY KEY'
print( conceptosPorgramacion )

print( '\nELIMINANDO DICCIONARIO' )
conceptosPorgramacion.clear()
print( conceptosPorgramacion )



# Listas
nombresList: list = [ 'Bryan', 'Ariel', 'Erick', 'Maria' ]
print( f'Nombres Usuarios: { nombresList }' )
print( f'Primer elemento de la lista de nombres: { nombresList[0] }' )
print( f'Ultimo elemento de la lista de nombres: { nombresList[-1] }' )
print( f'Penultimo elemento de la lista de nombres: { nombresList[-2] }' )
print( f'Accediendo a dos elementos de la lista de nombres (0-2): { nombresList[0:2] }' )
print( f'Accediendo a dos elementos de la lista de nombres (0-3 no incluir el tres): { nombresList[:3] }' )

# Cambiando un valor de una lista
nombresList[3] = 'Daniela'
print( f'Lista con nombre de la posicion 3 cambiado: { nombresList }' )

# Iterando una lista
for nombre in nombresList:
    print( f'Nombre Usuario: { nombre }' )

# Tamanio de la lista
print( f'El tamanio de la lista de nombres es: { len( nombresList ) }' )

# Operaciones con listas
'''Insertar elemento'''
nombresList.append( 'Goku' )
print( f'Append Goku: { nombresList }' )

'''Insertar elemento en un indice especifivo'''
nombresList.insert( 1, 'Vegeta' )
print( f'Insert vegeta en posicion 1: { nombresList }' )

'''Remover un elemento de la lista'''
nombresList.remove( 'Ariel' )
print( f'Removiendo Ariel de la lista: { nombresList }' )

'''Remover el ultimo elemento de la lista'''
nombresList.pop()
print( f'Removiendo ultimo elemento de la lista: { nombresList }' )

'''Removiendo elemento por indice'''
del nombresList[0]
print( f'Removiendo elemento de la lista 0: { nombresList }' )

'''Limpiar lista'''
nombresList.clear()
print( f'Limpiando lista: { nombresList }' )



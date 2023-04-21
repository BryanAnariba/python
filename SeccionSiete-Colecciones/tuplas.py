# la tupla guarda elementos pero solo modo lectura, ya no se pueden modificar, es inmutable, la lista es mutable
frutas: tuple = ( 'Naranja', 'Platano', 'Guayaba' )

print( f'Tamanio frutas: { len( frutas ) } - { frutas }' )

for fruta in frutas:
    print( f'Fruta: { fruta }' )
# Set es parecido a tuplas y listas pero no acepta repetidos o duplicados, set no lleva orden
planetas: set = { 'Tierra', 'Marte', 'Jupiter' }
planetas.add( 'Pluton' )
planetas.add( 'Pluton' ) # No agrega duplicados
print( planetas )

planetas.discard( 'Tierra' )
# Ver si un elemento esta en el set
print( 'Tierra' in planetas )
print( planetas )
# Crea un variable llamada conejos y asígnale el valor 126.
rabbits: int = 126

# Crea una variable llamada zanahorias y asígnale el valor 0
carrots: int = 0

# Muestra el contenido de la variable conejos.
print(f'Rabbits: {rabbits}')

# Modifica el valor de la variable conejos a 150
rabbits = 150

# Copia el valor de la variable conejos en la variable zanahorias
carrots = rabbits

# Imprime el valor de las dos variables con print().
print(f'Rabbits: {rabbits}, Carrots: {carrots}')

'''Modifica el valor de conejos por 250 y vuelve a mostrar las dos
variables'''
rabbits = 250
print(f'Rabbits: {rabbits}, Carrots: {carrots}')

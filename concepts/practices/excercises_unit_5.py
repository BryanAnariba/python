# Escribe la palabra elefante dentro de una variable llamada animal.
animal: str = "Elefante"
print(f'Animal: {animal}')

# Escribe la palabra rosa dentro de una variable llamada color.
color: str = 'Rosa'
print(f'Color: {color}')

'''
    Crea una variable llamada imagina donde se almacenen las dos variables
    anteriores: animal y color dando como resultado el valor elefanterosa.
'''
imagine: str = f'{animal}{color}'
print(f'Imagine: {imagine}')

'''
    En la variable imagina intercala un espacio en blanco para separar las dos
    palabras.
'''
imagine = f'{animal} {color}'
print(f'Imagine: {imagine}')

# Muestra la pregunta ¿Cuál es tu nombre? y almacénala en la variable
name: str = input('¿Cuál es tu nombre?\nR:// ')
print(f'Name: {name}')

'''
    Guarda la primera letra del contenido de la variable nombre dentro de la
    variable inicial.
'''
name = name[0:1]
print(name)

'''
    Dada la variable s = ‘Carlos Gomez Perez’ copia solo el nombre Gomez
    en una variable llamada m
'''
s: str = 'Carlos Gomez Perez'
m: str = s[s.index('Perez'): len(s)]
print(m)
"""
    Instrucciones de la tarea:
    El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
    El usuario proporcionará un valor entre 0 y 10.
    Si está entre 9 y 10: imprimir una A
    Si está entre 8 y menor a 9: imprimir una B
    Si está entre 7 y menor a 8: imprimir una C
    Si está entre 6 y menor a 7: imprimir una D
    Si está entre 0 y menor a 6: imprimir una F
    cualquier otro valor debe imprimir: Valor incorrecto
    Por ejemplo:
    Proporciona un valor entre 0 y 10:
    A
"""

calificacionEstudiante: float = float( input( 'Proporcione la nota del alumno: ' ) )
nota: str = None
if 9 <= calificacionEstudiante <= 10:
    nota = 'A'
elif 8 < calificacionEstudiante < 9:
    nota = 'B'
elif 7 < calificacionEstudiante < 8:
    nota = 'C'
elif 6 <= calificacionEstudiante < 7:
    nota = 'D'
elif 0 <= calificacionEstudiante < 6:
    nota = 'F'

print( f'Calificacion: { calificacionEstudiante } - Nota: { nota }' )
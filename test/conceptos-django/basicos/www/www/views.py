# Request: Sirve para realizar peticiones al servidor
# Response: Sirve para enviar respuesta por medio del protocolo http
from django.http import HttpResponse
import datetime

# ESTO ES UNA VISTA
def welcome( request ):
    return HttpResponse("Bienvenid(@) a este curso de Django")

def welcomeInRed( request ):
    return HttpResponse( "<p style='color: red;'>Bienvenid(@) a este curso de Django en Rojo</p>" )

def categoriaEdad( request, edad ):
    categoria: str = ''
    if edad >= 18:
        if edad >= 60:
            categoria = 'Tercera Edad'
        else:
            categoria = 'Es Adulto de Edad Mediana'
    else:
        if edad < 10:
            categoria = 'Es un chamaco'
        else:
            categoria = 'Es un Adolecente'

    response = f"<h2>Categoria de la edad es: { categoria }</h2>"
    return HttpResponse( response )

def obtenerHoraActual( request ):
    #response = f"<h2>La hora actual es: { datetime.datetime.now() }</h2>"
    response = f"<h2>La hora actual es: { datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S') }</h2>"
    return HttpResponse( response )
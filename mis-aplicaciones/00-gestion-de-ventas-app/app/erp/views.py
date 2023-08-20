from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from erp.models import Category

# Create your views here.
def primeraVista( request ):
    datos: dict = { "nombre": "Bryan Ariel", "apellido": "Sanchez Anariba" }
    return JsonResponse( datos )

def segundaVista( request ):
    datos: dict = { "nombre": "Maria Fernanda", "apellido": "Sanchez Anariba" }
    return JsonResponse( datos )

def terceraVista( request ):
    userData: dict = { 
        'user_name': 'saariel115@gmail.com', 
        'role': 'admin',
        'categories': Category.objects.all()
    }
    return render( 
        request, 'index.html', 
        userData
    )




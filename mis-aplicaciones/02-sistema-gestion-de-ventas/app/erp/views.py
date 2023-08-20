from django.shortcuts import render
from django.http import HttpResponse, request

from erp.models import Category

# Create your views here.

def indexView(request):
    categories = Category.objects.all()
    #print( f'categories: { categories }' )
    data: dict = {
        'name': 'Bryan Ariel',
        'lastName': 'Sanchez Anariba',
        'categories': categories
    }
    return render( request, 'index.html', data )

def myFirstView( request ):
    data: dict = {
        'name': 'Bryan Ariel',
        'lastName': 'Sanchez Anariba',
    }
    return HttpResponse( f'This is my first view { data }' )

def otherUserView( request ):
    data: dict = {
        'name': 'Bryan Ariel',
        'lastName': 'Sanchez Anariba',
    }
    return HttpResponse( f'This is other view { data }' )

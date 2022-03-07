from http.client import HTTPResponse
import json
from tkinter import E
from turtle import update
from django.views import View

# MY IMPORTATIONS
from .models import Company
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class CompanyView ( View ):

    @method_decorator( csrf_exempt )
    def dispatch( self, request, *args, **kwargs ):
        return super().dispatch(request, *args, **kwargs)
        
    def get( self, request, id=0 ):
        if id > 0:
            company = list( Company.objects.filter( id=id ).values() )
            if len( company ) > 0:
                datos = { 'status': 200, 'data': company[0] }
            else:
                datos = { 'status': 200, 'data': 'Company not found' }
            return JsonResponse( datos )
        else:
            companies = list( Company.objects.values() )
            if len( companies ) > 0:
                datos = { 'status': 200, 'data': companies }
            else:
                datos = { 'status': 200, 'data': 'No companies found' }
            return JsonResponse( datos )

    def post( self, request ):
        #print( request.body )

        # PARA LEER EL JSON EN PYTHON Y RECORRERLO COMO UN DICCIONARIO
        jsondata = json.loads( request.body )
        #print( jsondata )
        Company.objects.create(
            name = jsondata['name'],
            website = jsondata['website'],
            fundation = jsondata['foundation']
        )
        datos = { 'status': 201, 'data': 'Company ' + jsondata['website'] + ' created successfully' }
        return JsonResponse( datos )
        
    def put( self, request, id=0 ):
        if id == 0:
            datos = { 'status': 400, 'data': 'Company Id Is required' }
            return JsonResponse( datos )
        else:
            jsondata = json.loads( request.body )
            company = Company.objects.filter( id=id )
            if len( company ) > 0:
                updated = Company.objects.get( id=id )
                updated.name = jsondata[ 'name' ]
                updated.fundation = jsondata[ 'foundation' ]
                updated.website = jsondata[ 'website' ]

                # Guardamos cambios
                updated.save()

                datos = { 'status': 400, 'data': 'Company ' + jsondata[ 'name' ] + ' updated successfully' }
                return JsonResponse( datos )
            else:
                datos = { 'status': 400, 'data': 'Company not found' }
                return JsonResponse( datos )

    def delete( self, request, id = 0 ):
        if id != 0:
            company = list( Company.objects.filter( id=id ).values() )
            if len( company ) > 0:
                Company.objects.filter( id=id ).delete()
                datos = { 'status': 200, 'data': 'Company Delete Successfully' }
                return JsonResponse( datos )
            else:
                datos = HttpResponseBadRequest( { 'status': 400, 'data': 'Company Not Found' } )
                return JsonResponse( datos )
        else:
            datos = HttpResponseBadRequest({ 'status': 400, 'data': 'Company Id is required' })
            return JsonResponse( datos )

from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json

class CompanyView( View ):
    status: int
    companies: list
    company: dict

    @method_decorator( csrf_exempt )
    def dispatch( self, request, *args, **kwargs ):
        return super().dispatch(request, *args, **kwargs)

    def get( self, request, id = 0 ):
        if id > 0:
            self.companies = list( Company.objects.filter( id=id ).values() )
            if len( self.companies ):
                self.status = 200
                response = { 'status': self.status, 'data': self.companies[0] }
            else:
                self.status = 400
                response = { 'status': self.status, 'data': 'Company not found' }

        else:
            self.companies: list = list(Company.objects.values())
            if ( len( self.companies ) > 0 ):
                self.status = 200
                response = { 'status': self.status, 'data': self.companies }
            else:
                self.status = 400
                response = { 'status': self.status, 'data': 'Companies not found' }
        
        return JsonResponse( response, status = self.status )


    def post( self, request ):
        self.status = 201
        jsonDecode = json.loads( request.body )
        #print( jsonDecode )
        Company.objects.create( name = jsonDecode[ 'name' ], webSite = jsonDecode[ 'webSite' ], fundation = jsonDecode[ 'fundation' ] )
        response = { 'status': self.status, 'data': f"Company { jsonDecode[ 'name' ] } created." }
        return JsonResponse( response, status = self.status )

    def put( self, request, id ):
        jsonDecode = json.loads( request.body )
        self.companies = list( Company.objects.filter( id=id ).values() )
        if ( len( self.companies ) > 0 ):
            self.company = Company.objects.get( id=id )
            self.company.name = jsonDecode[ 'name' ]
            self.company.webSite = jsonDecode[ 'webSite' ]
            self.company.fundation = jsonDecode[ 'fundation' ]
            self.company.save()
            self.status = 200
            response = { 'status': self.status, 'data': f"Company { jsonDecode[ 'name' ] } updated." }
        else:
            self.status = 400
            response = { 'status': self.status, 'data': 'You can not update this company because not exists' }

        return JsonResponse( response, status = self.status )
    
    def delete( self, request, id ):
        self.companies = list( Company.objects.filter( id=id ).values() )
        if len( self.companies ) > 0:
            self.status = 200
            Company.objects.filter( id=id ).delete()
            response = { 'status': self.status, 'data': f"Company deleted." }
        else:
            self.status = 400
            response = { 'status': self.status, 'data': 'You can not delete this company because not exists' }

        return JsonResponse( response, status = self.status )
        

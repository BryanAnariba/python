from django.urls import path
from erp.views import primeraVista, segundaVista, terceraVista

urlpatterns = [
    path('vista-uno', primeraVista),
    path('vista-dos', segundaVista),
    path('vista-tres', terceraVista)
]
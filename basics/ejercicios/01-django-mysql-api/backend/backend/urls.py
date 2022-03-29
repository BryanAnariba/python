from django.contrib import admin

# MY IMPORTATIONS
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include( 'api.urls')) 
]

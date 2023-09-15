from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo), # http://localhost:8000/saludo
    path('despedida/', views.despedida), # http://localhost:8000/despedida
    path('users/<int:userId>', views.getUserData), # http://localhost:8000/users/10
    path('playlists/<int:playlistId>/songs/<int:songId>', views.getSongData) # http://localhost:8000/playlists/10/songs/1
]

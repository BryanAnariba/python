from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola Mundo!!!')

def despedida(request):
    return HttpResponse('Adiositooo!!')

def getUserData(request, userId):
    return HttpResponse(f'User with id { userId }')

def getSongData(request, playlistId, songId):
    return HttpResponse(f'Song { songId } in playlists { playlistId }')
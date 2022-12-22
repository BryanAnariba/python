from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# 2: 20

def hello( request, username: str ):
    return HttpResponse(f"<h1>Home { username }</h1>")

def courses( request, courseId: int ):
    return HttpResponse(f"<h1>Course Id { courseId }</h1>")

def projects( request ): #http://127.0.0.1:8000/api/projects/
    # Obtener todos los proyectos
    #projectsData = list(Project.objects.values())
    projectsData = Project.objects.all()
    response: dict = { "status": 200, "projects": projectsData}
    #return JsonResponse( response, status = 200, safe=False )
    return render( request, 'views/projects.html', { 'data': response })

def getTask( request, taskId: int ): #http://127.0.0.1:8000/api/tasks/1
    taskData = list(Task.objects.filter(id=taskId).values())
    response: dict = { "status": 200, "data": taskData[0]}
    return JsonResponse( response, status = 200, safe=False )

def getTaskByName( request, taskName: str ):
    taskData = list( Task.objects.filter( title__icontains=taskName ).values() )
    response: dict = { "status": 200, "data": taskData }
    return JsonResponse( response, status = 200, safe=False )

def tasks( request ): #http://127.0.0.1:8000/api/tasks/
    tasks = Task.objects.all()
    response: dict = { 'status': 200, 'tasks': tasks }
    return render( request, 'views/tasks.html', { 'data': response })

# RENDERIZANDO PLANTILLAS O HTML
def index( request ): #http://127.0.0.1:8000/api/
    title: str = 'Welcome To Django Course'
    return render( request, 'index.html', { 'title': title })

def about( request ): #http://127.0.0.1:8000/api/about
    userName: str = 'bsanchez'
    return render( request, 'views/about.html', { 'userName': userName })




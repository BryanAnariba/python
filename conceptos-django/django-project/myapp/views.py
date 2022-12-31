from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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
    return render( request, 'projects/projects.html', { 'data': response })

def getTask( request, taskId: int ): #http://127.0.0.1:8000/api/tasks/1
    taskData = list(Task.objects.filter(id=taskId).values())
    response: dict = { "status": 200, "data": taskData[0]}
    return JsonResponse( response, status = 200, safe=False )

def getTaskByName( request, taskName: str ): #http://127.0.0.1:8000/api/tasks/search/Fundamentos JS
    taskData = list( Task.objects.filter( title__icontains=taskName ).values() )
    response: dict = { "status": 200, "data": taskData }
    return JsonResponse( response, status = 200, safe=False )

def tasks( request ): #http://127.0.0.1:8000/api/tasks/
    tasks = Task.objects.all()
    response: dict = { 'status': 200, 'tasks': tasks }
    return render( request, 'tasks/tasks.html', { 'data': response })

# RENDERIZANDO PLANTILLAS O HTML
def index( request ): #http://127.0.0.1:8000/api/
    title: str = 'Welcome To Django Course'
    return render( request, 'index.html', { 'title': title })

def about( request ): #http://127.0.0.1:8000/api/about
    userName: str = 'bsanchez'
    return render( request, 'views/about.html', { 'userName': userName })

def createTask( request ): #http://127.0.0.1:8000/api/tasks/create?title=BRR&description=BR%0D%0A
    #print( request.GET[ 'title' ] )
    #print( request.GET[ 'description' ] )
    if request.method  == 'GET':
        return render( request, 'tasks/create-task.html', { 'form': CreateNewTask })
    else:
        Task.objects.create(
            title = request.POST[ 'title' ],
            description = request.POST[ 'description' ],
            project_id=1
        )
        return redirect( '/api/tasks' )

def createProject( request ):
    if request.method == 'GET':
        return render( request, 'projects/create-project.html', { 'form': CreateNewProject } )
    else:
        Project.objects.create(
            name = request.POST[ 'name' ]
        )
        return redirect( '/api/projects' )


        




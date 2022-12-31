from django.urls import path
from .views import hello, about, index, courses, projects, tasks, getTask, getTaskByName, createTask, createProject

urlpatterns = [
    path( '', index ),
    path( 'about/', about ),
    path( 'hello/<str:username>', hello ), #http://127.0.0.1:8000/api/hello/Bryan
    path( 'courses/<int:courseId>', courses ),
    path( 'projects/', projects ),
    path( 'projects/create/', createProject, name='createproject' ),
    path( 'tasks/', tasks, name='task'),
    path( 'tasks/<int:taskId>', getTask),
    path( 'tasks/create', createTask, name='createtask' ),
    path( 'tasks/search/<str:taskName>', getTaskByName ),
]
from django.contrib import admin
from .models import Project, Task

# esto de aqui es para que lo reconozca en el panel de admin django
admin.site.register( Project )
admin.site.register( Task )

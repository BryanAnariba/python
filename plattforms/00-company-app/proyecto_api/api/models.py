from django.db import models

class Company( models.Model ):
    name = models.CharField( max_length = 50 )
    webSite = models.URLField( max_length = 100 )
    fundation = models.PositiveIntegerField()


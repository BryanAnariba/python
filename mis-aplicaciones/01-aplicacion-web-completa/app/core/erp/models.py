from django.db import models
import datetime

class EmployeeType( models.Model ):
    employee_type = models.CharField( max_length=100, verbose_name='Employee Type' ) # unique=True

    def __str__(self) -> str:
        return self.employee_type
    
    class Meta():
        verbose_name = 'EmployeeType'
        verbose_name_plural = 'EmployeesTypes'
        db_table='EmployeeType'
        ordering = ['id']

# Create your models here.
class Employee( models.Model ):
    '''
        Relacion m: 1 muchos empleados tienenun tipo de empleado = 
        models.CASCADE es que si elimino tipos de empleados se van todos los empleados que usen id de tipo empleado, 
        models.PROTECTED no permite borrar
        ver el video 9 para ver las relaciones muchos a muchos
    '''
    employee_type = models.ForeignKey( EmployeeType, on_delete=models.PROTECT )
    first_name = models.CharField( max_length=100, verbose_name='First Name' )
    last_name = models.CharField( max_length=100, verbose_name='Last Name' )
    date_joined = models.DateField( default=datetime.datetime.now, verbose_name='Register Date' )
    created_at = models.DateTimeField( auto_now=True  )
    updated_at = models.DateTimeField( auto_now_add=True  )
    age = models.PositiveIntegerField( default=0 )
    salary = models.DecimalField( default=0.00, max_digits=15, decimal_places=2 )
    status = models.BooleanField( default=True )
    avatar = models.ImageField( upload_to='avatar/%Y/%m/%d' )
    curriculum_vitae = models.ImageField( upload_to='curriculum_vitae/%Y/%m/%d' )
    gender = models.CharField( max_length=1 )

    def __str__(self) -> str:
        return ( self.first_name + '  ' + self.last_name )
    
    class Meta():
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table='Employee'
        ordering = ['id']
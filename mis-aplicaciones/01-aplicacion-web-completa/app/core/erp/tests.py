from models import EmployeeType

# Listado
try:
    query = EmployeeType.objects.all()
    print( query )
except Exception as ex:
    print( f'Error { ex }' )

# Creacion
try:
    newEmployee = EmployeeType()
    newEmployee.employee_type = 'Gerente'
    newEmployee.save()
except Exception as ex:
    print( f'Error { ex }' )

# Edicion
try:
    updateEmployee = EmployeeType.objects.get(id=1)
    updateEmployee.employee_type = 'Gerente'
    updateEmployee.save()
except Exception as ex:
    print( f'Error { ex }' )

# Eliminacion mejor hacerlo soft delete
# updateEmployee = EmployeeType.objects.delete(id=1)

#
# try:
#     #result = EmployeeType.objects.filter()
#     #print( result )
# except Exception as ex:
#     print( f'Error { ex }' )



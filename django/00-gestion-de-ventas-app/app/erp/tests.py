from models import Category
# from django.test import TestCase

''' Operaciones Crud en Category '''

# Listado
categories = Category.objects.all()
print( categories )

# Creacion
newCategory = Category( "Gerente", "Permisos globales en la aplicacion" )
newCategory.save()

# Actualizacion
category = Category.objects.get( id=1 )
category.category_name = "Gerente Modificado"
category.category_desc = "Permisos globales en la aplicacion Modificado"
category.save()


# Eliminacion para mi mejor un soft delete
try:
    itemSelected = Category.objects.get( id=1 )
    itemSelected.delete()
except Exception as ex:
    print( f'Error SQL Query: { ex }' )

''' Consultas adicionales '''
categoriesWithGe = Category.objects.filter( category_name__contains='Ge' ) # Registros que contengan Ge
viewSQLQueryCategoriesWithGe = Category.objects.filter( category_name__contains='Ge' ).query # Para ver la consulta sql
categoriesStartWithG = Category.objects.filter( category_name__startswith='G' ) # Registros que inicien en G
categoriesInGerenteAdmin = Category.objects.filter( category_name__in=['Gerente', 'Admin'] ) # Registros que el nombre este en Gerente, Admin
categoriesInGerenteAdminCount = Category.objects.filter( category_name__in=['Gerente', 'Admin'] ).count()


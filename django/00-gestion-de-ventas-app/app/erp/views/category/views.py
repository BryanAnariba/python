from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.http import request
from erp.models import Category

# Vista Basada en Funcion
def category_list( request ):
    data = { 'titulo': 'Listado De Categorias', 'categories': Category.objects.all() }
    return render( request, 'category/list.html', data )

# Vista Basada en Clases "Asi Exprimimos mas lo que nos da Django"
class CategoryListView( ListView ):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = { 'category_name': 'Books', 'category_desc': 'For Students' }
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado De Categorias'
        return context

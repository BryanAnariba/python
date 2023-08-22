from django.urls import path
from erp.views.category.views import category_list, CategoryListView

urlpatterns = [
    path('categories/', category_list),
    path('categories/list/', CategoryListView.as_view())
]
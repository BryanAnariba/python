from django.urls import path
from erp.views import myFirstView, otherUserView, indexView

urlpatterns = [
    path('', indexView ),
    path('my-first-view', myFirstView),
    path('other-user-route', otherUserView )
]
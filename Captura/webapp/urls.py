from django.urls import path
from .views import categorias,base
app_name = 'webapp'
urlpatterns = [
    path('',base,name="base"),
    path('categorias/<int:pk>',categorias,name='categorias'),
]

from django.shortcuts import render
from .models import Categoria,CategoriaImg



def base(request):
    categorias = Categoria.objects.all()    

    return render(request,'index.html',{'categorias':categorias})

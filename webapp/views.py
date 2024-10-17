from django.shortcuts import render
from .models import Portada,Categoria,ImgCategoria



def base(request):
    portadas = Portada.objects.all() 
    categorias = Categoria.objects.all()
    return render(request,'index.html',{'categorias':categorias,'portadas':portadas,'active_page':'base'})

def categorias(request,pk):
    categoria = Categoria.objects.get(pk=pk)
    imgsCategoria = ImgCategoria.objects.filter(categoria=categoria)
    
    return render(request,'categorias.html',{'imgsCategoria':imgsCategoria,'active_page':'categorias'})
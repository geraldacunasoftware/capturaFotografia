from django.contrib import admin
from .models import Categoria,Producto,CategoriaImg,ProductoImg,Blog,BlogImg

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(CategoriaImg)
admin.site.register(ProductoImg)
admin.site.register(Blog)
admin.site.register(BlogImg)
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.nombre} - {self.id}'

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} '

class CategoriaImg(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/categoriaImg')
    
    def __str__(self):
        return f'img categoria: {self.categoria.nombre} - categoria id- {self.categoria.id}'
    
class ProductoImg(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/productoImg')
    
    def __str__(self):
        return f'img producto: {self.producto.nombre}'    

class Blog(models.Model):
    titulo = models.CharField(max_length=255)
    entrada = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.titulo}'
    
class BlogImg(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/blogImg')
    
    def __str__(self):
        return f'img de blog {self.blog.titulo}'
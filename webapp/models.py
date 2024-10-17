from django.db import models
from PIL import Image
from django.core.files.storage import default_storage

class Portada(models.Model):
    img = models.ImageField(upload_to='media/Portadas')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda la imagen original primero

        image_path = self.img.path
        img = Image.open(image_path)

        # Definir el tamaño exacto
        output_size = (1200, 600)

        # Redimensionar la imagen
        img = img.resize(output_size)

        # Recortar la imagen al centro si no tiene la proporción exacta
        img_width, img_height = img.size
        left = (img_width - output_size[0]) / 2
        top = (img_height - output_size[1]) / 2
        right = (img_width + output_size[0]) / 2
        bottom = (img_height + output_size[1]) / 2
        img = img.crop((left, top, right, bottom))

        # Sobrescribir la imagen con el nuevo tamaño
        img.save(image_path)


class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    img = models.ImageField(upload_to='media/FotoPrincipal',null=True)

    def __str__(self):
        return f'{self.nombre} - id: {self.id}'

class ImgCategoria(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/Categorias')
    
    def __str__(self):
        return f'{self.categoria.nombre} - id: {self.categoria.id}'
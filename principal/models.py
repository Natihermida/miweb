from django.db import models

# Create your models here.
from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/')
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre


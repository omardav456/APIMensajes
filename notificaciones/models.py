from django.db import models

# Create your models here.

class Notificacion (models.Model):
    titulo= models.CharField(max_length=100)
    mensaje= models.TextField()
    emisor= models.TextField(max_length=100)
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    activa= models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
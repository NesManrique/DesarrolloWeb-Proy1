from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class error(models.Model):
    estado = models.CharField( max_length = 15)
    duplicado = models.ForeignKey('self', null=True)
    prioridad = models.IntegerField()
    fecha_reporte = models.DateTimeField(auto_now_add = True) 
    usuario_reporte = models.ForeignKey(User, related_name = 'reportero')
    fecha_modif = models.DateTimeField(auto_now = True, null = True)
    usuario_encargado = models.ForeignKey(User, related_name = 'encargado', null=True)
    info_duplicacion = models.TextField()
    
    
    

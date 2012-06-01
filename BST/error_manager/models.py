from django.db import models
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 

ESTADO_CHOICES = (
    ('Sin Confirmar','Sin Confirmar'),
    ('Asignado','Asignado'),
    ('Resuelto','Resuelto'),
    ('Duplicado','Duplicado'),
    ('Cerrado','Cerrado')
)

class Error(models.Model):
    titulo = models.CharField(max_length = 20)
    estado = models.CharField(max_length = 13, choices=ESTADO_CHOICES, default='Sin Confirmar')
    duplicado = models.ForeignKey('self', null=True, default=None)
    prioridad = models.IntegerField()
    fecha_reporte = models.DateTimeField(auto_now_add = True) 
    usuario_reporte = models.ForeignKey(User, related_name = 'reportero')
    fecha_modif = models.DateTimeField(auto_now = True, null = True)
    usuario_encargado = models.ForeignKey(User, related_name = 'encargado', null=True, default=None)
    info_duplicacion = models.TextField(blank=True, default="")
   
    def __unicode__(self):
        return self.titulo

class Tag(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    errores = models.ManyToManyField(Error)

    def __unicode__(self):
        return self.nombre
    
class ErrorsListView(ListView):
    context_object_name = "error_list"
    template_name = "errores_page.html"

    def get_queryset(self):
        return Error.objects.all()
    

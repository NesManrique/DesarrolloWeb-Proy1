from django import forms
import re
from django.contrib.auth.models import User

ESTADO_CHOICES = (
    ('Sin Confirmar','Sin Confirmar'),
    ('Asignado','Asignado'),
    ('Resuelto','Resuelto'),
    ('Duplicado','Duplicado'),
    ('Cerrado','Cerrado')
)

msjs_error_save = {
    'required' : 'Este campo es obligatorio.',
    'invalid' : 'Valor invalido. Por favor inserte un valor de prioridad del 1 al 5.',
    'max_value' : 'La prioridad debe tener un valor maximo de 5.',
    'min_value' : 'La prioridad debe tener un valor minimo de 1.'
}

msjs_error_estado = {
    'required' : 'Este campo es obligatorio.',
    'invalid_choice' : 'Elija una de las opciones'
}

class ErrorSaveForm(forms.Form):
    titulo = forms.CharField(
        label = u'Titulo', 
        widget = forms.TextInput(attrs={'size':64})
    )

    prioridad = forms.IntegerField(
        label = u'Prioridad',
        min_value=1,
        max_value=5,
        error_messages=msjs_error_save
    )
    tags = forms.CharField(
        label = u'Tags',
        required = False,
        widget = forms.TextInput(attrs={'size':60})
    )

class ErrorUpEstado(forms.Form):
    Estado = forms.ChoiceField(
        label = u'Estado',
        choices=ESTADO_CHOICES,
        error_messages=msjs_error_estado
    )

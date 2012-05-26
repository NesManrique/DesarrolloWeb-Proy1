# Create your views here.
from django.contrib.auth.models import User
from user_manager.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from error_manager.models import Error
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.comments.models import Comment

def error_save(request):
    if request.method == 'POST':
        form = ErrorSaveForm(request.POST)
        if form.is_valid():
            error, created = Error.objects.get_or_create(
                titulo = form.cleaned_data['titulo'],
                estado = form.cleaned_data['estado'],
                duplicado = None,
                prioridad = form.cleaned_data['prioridad'],
                usuario_reporte = request.user,
                usuario_encargado = None,
                info_duplicacion = 'prueba'
            )
            return HttpResponse('/users/%s/' % request.user.username)
    else:
        form = ErrorSaveForm()
        
    variables = RequestContext(request, {'form': form })
    return render_to_response('error_save.html', variables)
                
                
                    
            

        
    

# Create your views here.
from django.contrib.auth.models import User
from user_manager.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from error_manager.models import Error, Tag
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
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
            
            if not created:
                error.tag_set.clear()

            lista_tags = form.cleaned_data['tags'].split()
            for tag_nombre in lista_tags:
                tag, var = Tag.objects.get_or_create(nombre=tag_nombre)
                error.tag_set.add(tag)
            error.save() 
            return HttpResponseRedirect('/error/save/exitoso')
    else:
        form = ErrorSaveForm()
        
    variables = RequestContext(request, {'form': form })
    return render_to_response('error_save.html', variables)
    
@login_required            
def error_list(request, username):
    user = User.objects.get(username=username)
    error_list = user.encargado.all()
    lista = RequestContext(request, {'error_listu': error_list})
    return render_to_response('errores_page.html', lista)        
                    
def tag_page(request, tag_name):
    tag = get_object_or_404(Tag, nombre=tag_name)
    errores = tag.errores.order_by('-id')
    variables = RequestContext(request, {
        'error_list': errores,
        'tag_name': tag_name
    })
    return render_to_response('tag_page.html', variables) 

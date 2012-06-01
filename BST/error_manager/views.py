# Create your views here.
from django.contrib.auth.models import User
from error_manager.forms import *
from django.template import RequestContext
from error_manager.models import Error, Tag
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, get_object_or_404
from error_manager.models import Error
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from django.utils.simplejson import dumps
from django.views.generic import DetailView

@login_required
def error_save(request):
    if request.method == 'POST':
        form = ErrorSaveForm(request.POST)
        if form.is_valid():
            error, created = Error.objects.get_or_create(
                titulo = form.cleaned_data['titulo'],
                prioridad = form.cleaned_data['prioridad'],
                usuario_reporte = request.user,
            ) 
            
            if not created:
                error.tag_set.clear()

            lista_tags = form.cleaned_data['tags'].split()
            for tag_nombre in lista_tags:
                tag, var = Tag.objects.get_or_create(nombre=tag_nombre)
                error.tag_set.add(tag)
            error.save() 
            
            return HttpResponseRedirect(reverse("user_page"))
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

def asignar_enc(request, error_id):
    if request.method == 'POST':
        usuario = request.POST["lookuser"]
        err = get_object_or_404(Error, id=error_id)
        err.usuario_encargado_id = User.objects.get(username = usuario)
        err.estado = 'Asignado'
        err.save()
    return HttpResponseRedirect(reverse("error_detail", args=(error_id,)))

def asignar_estado(request, error_id):
    if request.method == 'POST':
        estado = request.POST['upestado'] 
        print estado
        err = get_object_or_404(Error, id=error_id)
        err.estado = estado
        err.save()
        return HttpResponseRedirect(reverse("error_detail", args=(error_id,)))

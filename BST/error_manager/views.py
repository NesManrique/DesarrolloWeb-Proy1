# Create your views here.
from django.contrib.auth.models import User
from user_manager.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from error_manager.models import Error
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from django.utils.simplejson import dumps

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
            return HttpResponseRedirect(reverse("user_page"))
    else:
        form = ErrorSaveForm()
        
    variables = RequestContext(request, {'form': form })
    return render_to_response('error_save.html', variables)


def asignar_enc(request, error_id):
    if request.method == 'POST':
        usuario = request.POST["lookuser"]
        err = get_object_or_404(Error, id=error_id)
        err.usuario_encargado_id = User.objects.get(username = usuario)
        err.save()
    return HttpResponseRedirect(reverse("error_detail", args=(error_id,)))

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.views import logout, login
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from user_manager.forms import *

def main_page(request):
    return render_to_response(
        'main_page.html', RequestContext(request)
    )

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user_page'))
    else:
        return login(request)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def users(request):
    username = request.user.username
    url = '/users/%s/' % username
    return HttpResponseRedirect(url)

@login_required
def user_page(request, username):
    try:
        user = User.objects.get(username=username)  
    except User.DoesNotExist:
        raise Http404(u'User not found')

    if(username != request.user.username):
        url = '/users/%s/' % request.user.username
        return HttpResponseRedirect(url)

    errors = user.reportero.all()
        
    variables = RequestContext(request, {
        'username': username,
        'errors': errors
    })

    return render_to_response('user_page.html', variables)

def register_page(request):
    print "hola"
    if request.method == 'POST': # Si el form ha sido presentado
        form =  RegistrationForm(request.POST) # un formulario dependiente de los datos del POST
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('users/registro/exitoso/')
    else:
        form = RegistrationForm() 
    
    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response(
        'registration/register.html',
        variables
    )
 
def user_lookup(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        users = User.objects.filter(username__icontains = q )[:20]
        results = []
        for user in users:
            user_json = {}
            user_json['label'] = user.username
            user_json['value'] = user.username
            results.append(user_json)
        data = simplejson.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


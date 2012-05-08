# Create your views here.
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello World")

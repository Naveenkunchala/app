from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app2(request):
    return HttpResponse('<h1>App2 is created</h1>')

def app2(request):
    return HttpResponse('<h1>App2 is created 2</h1>')

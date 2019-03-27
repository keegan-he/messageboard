from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(*args, **kwargs):
    print('running the home function')
    return HttpResponse("<h1>HELLOOO WORLDDDD!!!!</h1>")
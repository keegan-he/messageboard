from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>HELLOOO WORLDDDD!!!!</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page!!!!!!!</h1>")

def about_view(*args, **kwargs):
    return HttpResponse("<h1>Here is the about page!</h1>")
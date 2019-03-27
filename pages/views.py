from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact page!!!!!!!</h1>")

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>Here is the about page!</h1>")
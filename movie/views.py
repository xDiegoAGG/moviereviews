# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Diego Gonzalez'})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
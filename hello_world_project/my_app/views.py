from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola mundo, soy Evelyn, y este es mi examen")
# Create your views here.

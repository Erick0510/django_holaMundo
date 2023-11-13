from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola mundo, soy Erick")
# Create your views here.

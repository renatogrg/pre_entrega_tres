from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Carro
from django.shortcuts import render, redirect
# from inicio.forms import CreacionAnimalFormulario, BuscarAnimal

# Create your views here.

def mi_inicio(request):
    print('PASE POR ACA!!!!!')
    # return HttpResponse('<h1>Mi primera vista</h1>')
    return render(request, 'inicio/inicio.html')


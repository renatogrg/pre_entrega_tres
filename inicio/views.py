from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Carro
from django.shortcuts import render, redirect
from inicio.forms import CreacionCarroFormulario, BuscarCarro


# Create your views here.

def mi_inicio(request):
    print('PASE POR ACA!!!!!')
    # return HttpResponse('<h1>Mi primera vista</h1>')
    return render(request, 'inicio/inicio.html')

def crear_carro(request):
    if request.method == "POST":
        formulario = CreacionCarroFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            carro = Carro(modelo=datos_correctos['modelo'], marca=datos_correctos['marca'],precio=datos_correctos['precio'],año_fabricacion=datos_correctos['año_fabricacion'])
            carro.save()
            return redirect('inicio:listar_carros')
    
    formulario = CreacionCarroFormulario()
    return render(request, 'inicio/crear_carro.html', {'formulario': formulario})

def lista_carros(request):
    modelo_a_buscar = request.GET.get('modelo', None)
    if modelo_a_buscar:
        carros = Carro.objects.filter(modelo__icontains=modelo_a_buscar)
    else:
        carros = Carro.objects.all()
    formulario_busqueda = BuscarCarro()
    return render(request, 'inicio/lista_carros.html', {'carros': carros, 'formulario': formulario_busqueda})
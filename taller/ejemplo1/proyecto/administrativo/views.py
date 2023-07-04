from django.shortcuts import render, redirect
from django.shortcuts import render

from administrativo.models import *

from administrativo.forms import *

# Create your views here.

def index(request): 
    edificio = Edificio.objects.all()
    informacion_template = {'edificios': edificio}
    return render(request, 'index.html', informacion_template)


def obtenerEdificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificio': edificio}
    return render(request, 'obtenerEdificio.html', informacion_template)

def obtenerDepartamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    informacion_template = {'departamento': departamento}
    return render(request, 'obtenerDepartamento.html', informacion_template)

# CRUD Edificio
def agregarEdificio(request):

    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'aggEdificio.html', diccionario)


def editarEdificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editEdificio.html', diccionario)


def eliminarEdificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

# CRUD Departamento
def agregarDepartamento(request):

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'aggDepartamento.html', diccionario)


def editarDepartamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editDepartamento.html', diccionario)

def eliminarDepartamento(request, id):
    departamento= Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)
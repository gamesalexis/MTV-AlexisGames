from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Context, Template, loader

def familiaresModel(request):
    papa=FamiliaresModel(nombre="Fernando", edad=64, nacimiento='1958-04-25')
    mama=FamiliaresModel(nombre="Beatriz", edad=67, nacimiento='1954-09-10')
    hijo=FamiliaresModel(nombre="Alexis", edad=31, nacimiento='1991-01-06')
    papa.save()
    mama.save()
    hijo.save()
    diccionario={
                'Familiar_1':(papa.nombre, papa.edad, papa.nacimiento), 
                'Familiar_2':(mama.nombre, mama.edad, mama.nacimiento),  
                'Familiar_3':(hijo.nombre, hijo.edad, hijo.nacimiento),
                }
    plantilla=loader.get_template("vista.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def familiaresModel(request):
    papa=FamiliaresModel(nombre="Fernando", edad=64, nacimiento='1958-04-25')
    mama=FamiliaresModel(nombre="Beatriz", edad=67, nacimiento='1954-09-10')
    hijo=FamiliaresModel(nombre="Alexis", edad=31, nacimiento='1991-01-06')
    papa.save()
    mama.save()
    hijo.save()
    return render (request, "vista.html")
    
    
    
    #texto=f"hola mundo"
    #return HttpResponse(texto)
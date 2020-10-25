from django.shortcuts import render
from django.utils import timezone
from .models import Propiedad


def lista_propiedades(request):
	objetos = Propiedad.objects.all()
	return render(request, 'propiedad/propiedades.html',{'objetos':objetos})

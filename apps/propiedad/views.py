from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Propiedad
from django.views.generic import TemplateView

class Index(TemplateView):
	template_name = 'index.html'

def lista_propiedades(request):
	objetos = Propiedad.objects.all()
	return render(request, 'propiedad/propiedades.html',{'objetos':objetos})

def prop_detail(request, pk):
	propiedad = Propiedad.objects.get(pk=pk)
	return render(request, 'propiedad/prop_detail.html', {'propiedad':propiedad})





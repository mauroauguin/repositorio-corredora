from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Propiedad
from django.views.generic import TemplateView
from .forms import PropiedadForm

class Index(TemplateView):
	template_name = 'index.html'

def lista_propiedades(request):
	objetos = Propiedad.objects.all()
	return render(request, 'propiedad/propiedad.html',{'objetos':objetos})

def prop_detail(request, pk):
	propiedad = Propiedad.objects.get(pk=pk)
	return render(request, 'propiedad/prop_detail.html', {'propiedad':propiedad})

def nueva_propiedad(request):

    if request.method == "POST":
        form = PropiedadForm(request.POST)
        
        if form.is_valid():
            propiedad = form.save(commit=False)
            propiedad.usuario = request.user
          
            propiedad.save()

            return redirect('detail', pk=propiedad.pk)
    else:
        
        form = PropiedadForm()
        return render(request, 'propiedad/editar_propiedad.html', {'form': form})




def editar_propiedad(request, pk):

    propiedad = get_object_or_404(Propiedad, id=pk)
    if request.method == "POST":
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            propiedad = form.save(commit=False)
            propiedad.usuario = request.user
          
            propiedad.save()
            return redirect('detail', pk=propiedad.pk)
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'propiedad/editar_propiedad.html', {'form': form})
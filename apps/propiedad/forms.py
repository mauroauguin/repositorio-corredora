from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
	class Meta:
		model = Propiedad
		fields = ['direccion', 'comuna', 'tipo']
		
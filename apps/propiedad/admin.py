from django.contrib import admin
from .models import Propiedad, Propietario, Arrendatario, Arriendo

admin.site.register(Propiedad)
admin.site.register(Arriendo)
admin.site.register(Propietario)
admin.site.register(Arrendatario)
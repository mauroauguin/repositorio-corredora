from django.urls import path
from . import views

urlpatterns = [
    path('propiedades/', views.lista_propiedades, name='propiedades'),
]


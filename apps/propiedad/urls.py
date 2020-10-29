from django.urls import path
from . import views

urlpatterns = [
    path('propiedad/', views.lista_propiedades, name='propiedad'),
    path('propiedad/detail/<int:pk>/', views.prop_detail, name='detail'),
    path('propiedad/new/', views.nueva_propiedad, name='new'),
    path('propiedad/edit/<int:pk>/', views.editar_propiedad, name='edit'),
   
]


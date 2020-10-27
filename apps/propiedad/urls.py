from django.urls import path
from . import views

urlpatterns = [
    path('propiedades/', views.lista_propiedades, name='propiedades'),
    path('prop_detail/<int:pk>/', views.prop_detail, name='prop_detail'),
]


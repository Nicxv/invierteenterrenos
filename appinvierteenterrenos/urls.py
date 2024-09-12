
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),  # Página de inicio
    path('terrenos/', views.terrenos, name='terrenos'),  
    path('asesores/', views.asesores, name='asesores'),  
    
]
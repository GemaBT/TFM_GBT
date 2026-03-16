from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),         # http://127.0.0.1:8000/
    path('usuarios/', views.usuarios),  # http://127.0.0.1:8000/usuarios/
]
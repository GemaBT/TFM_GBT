"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),         # http://127.0.0.1:8000/
    path('usuarios/', views.usuarios),  # http://127.0.0.1:8000/usuarios/
]
"""
"""
from django.urls import path
from .views import usuarios, usuario_detalle

urlpatterns = [
    # Ruta para listar todos los usuarios o crear uno nuevo
    path('usuarios/', usuarios, name='usuarios'),

    # Ruta para ver, actualizar o eliminar un usuario específico
    path('usuarios/<int:pk>/', usuario_detalle, name='usuario_detalle'),
]
"""
from django.urls import path
from .views import (
    listar_usuarios, crear_usuario, obtener_usuario, actualizar_usuario, eliminar_usuario,
    listar_roles, crear_rol, obtener_rol, actualizar_rol, eliminar_rol,
    listar_permisos, crear_permiso, obtener_permiso, actualizar_permiso, eliminar_permiso
)

urlpatterns = [
    # USUARIOS
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/', obtener_usuario, name='obtener_usuario'),
    path('usuarios/<int:pk>/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/<int:pk>/eliminar/', eliminar_usuario, name='eliminar_usuario'),

    # ROLES
    path('roles/', listar_roles, name='listar_roles'),
    path('roles/crear/', crear_rol, name='crear_rol'),
    path('roles/<int:pk>/', obtener_rol, name='obtener_rol'),
    path('roles/<int:pk>/actualizar/', actualizar_rol, name='actualizar_rol'),
    path('roles/<int:pk>/eliminar/', eliminar_rol, name='eliminar_rol'),

    # PERMISOS
    path('permisos/', listar_permisos, name='listar_permisos'),
    path('permisos/crear/', crear_permiso, name='crear_permiso'),
    path('permisos/<int:pk>/', obtener_permiso, name='obtener_permiso'),
    path('permisos/<int:pk>/actualizar/', actualizar_permiso, name='actualizar_permiso'),
    path('permisos/<int:pk>/eliminar/', eliminar_permiso, name='eliminar_permiso'),
]
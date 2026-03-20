from rest_framework import serializers
from .models import Usuario

from rest_framework import serializers
from .models import Usuario, Rol, Permiso

# ========================
# USUARIO
# ========================
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # incluye todos los campos de tu tabla users

# ========================
# ROL
# ========================
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

# ========================
# PERMISO
# ========================
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'
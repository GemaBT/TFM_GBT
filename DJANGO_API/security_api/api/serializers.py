"""
from rest_framework import serializers
from .models import Usuario
"""
from rest_framework import serializers
from .models import Usuario, Rol, Permiso
from .models import UserSession, AuthLog

# ========================
# USUARIO
# ========================
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # incluye todos los campos de tu tabla users

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("El email debe ser válido.")
        return value

    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El username debe tener al menos 3 caracteres.")
        return value

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


# ========================
# USER SESSION
# ========================
class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = '__all__'


# ========================
# AUTH LOG
# ========================
class AuthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthLog
        fields = '__all__'
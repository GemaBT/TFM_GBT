from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Rol, Permiso, UserSession, AuthLog, RolPermiso
from .serializers import (
    UsuarioSerializer,
    RolSerializer,
    PermisoSerializer,
    UserSessionSerializer,
    AuthLogSerializer,
)

# ========================
# UTILIDADES
# ========================

def check_role_permission(user, permiso_id):
    """
    Verifica si el usuario tiene un permiso según su rol.
    """
    try:
        rol_id = Usuario.objects.get(id=user.id).role_id
        return RolPermiso.objects.filter(role_id=rol_id, permission_id=permiso_id).exists()
    except Usuario.DoesNotExist:
        return False

# ========================
# USUARIOS
# ========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuarios(request):
    if not check_role_permission(request.user, permiso_id=1):  # ID del permiso "listar usuarios"
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_usuario(request):
    if not check_role_permission(request.user, permiso_id=2):  # ID "crear usuario"
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_usuario(request, pk):
    if not check_role_permission(request.user, permiso_id=3):  # ID "ver usuario"
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_usuario(request, pk):
    if not check_role_permission(request.user, permiso_id=4):  # ID "editar usuario"
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_usuario(request, pk):
    if not check_role_permission(request.user, permiso_id=5):  # ID "eliminar usuario"
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ========================
# ROLES
# ========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_roles(request):
    if not check_role_permission(request.user, permiso_id=6):
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    roles = Rol.objects.all()
    serializer = RolSerializer(roles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_rol(request):
    if not check_role_permission(request.user, permiso_id=7):
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    serializer = RolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_rol(request, pk):
    if not check_role_permission(request.user, permiso_id=8):
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    try:
        rol = Rol.objects.get(pk=pk)
    except Rol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RolSerializer(rol, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_rol(request, pk):
    if not check_role_permission(request.user, permiso_id=9):
        return Response({"detail": "No autorizado"}, status=status.HTTP_403_FORBIDDEN)

    try:
        rol = Rol.objects.get(pk=pk)
    except Rol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    rol.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ========================
# PERMISOS
# ========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_permisos(request):
    permisos = Permiso.objects.all()
    serializer = PermisoSerializer(permisos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_permiso(request):
    serializer = PermisoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========================
# USER SESSIONS
# ========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_sesiones(request):
    sesiones = UserSession.objects.all()
    serializer = UserSessionSerializer(sesiones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_sesion(request):
    serializer = UserSessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========================
# AUTH LOGS
# ========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_logs(request):
    logs = AuthLog.objects.all()
    serializer = AuthLogSerializer(logs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_log(request):
    serializer = AuthLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
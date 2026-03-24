from rest_framework import permissions
from .models import RolPermiso, Usuario

class RolPermisoPermission(permissions.BasePermission):
    """
    Permite acceso solo si el usuario tiene permiso según rol.
    """

    def has_permission(self, request, view):
        # usuario autenticado
        user = request.user
        if not user.is_authenticated:
            return False

        # obtener rol_id del usuario
        try:
            rol_id = Usuario.objects.get(id=user.id).role_id
        except Usuario.DoesNotExist:
            return False

        # mapear la vista con nombre de permiso
        permiso_name = view.permission_name if hasattr(view, 'permission_name') else None
        if not permiso_name:
            return True  # si no hay permiso definido, acceso permitido

        # verificar si el rol tiene el permiso
        permisos = RolPermiso.objects.filter(role_id=rol_id)
        return permisos.filter(permission_id__in=[p.id for p in permiso_name]).exists()
from django.db import models

# ========================
# Tabla Users
# ========================
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    role_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'users'   # coincide con tu tabla MySQL
        managed = False      # Django no creará la tabla

    def __str__(self):
        return self.username


# ========================
# Tabla Roles
# ========================
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'roles'
        managed = False

    def __str__(self):
        return self.name


# ========================
# Tabla Permissions
# ========================
class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'permissions'
        managed = False

    def __str__(self):
        return self.name


# ========================
# Tabla role_permissions
# ========================
class RolPermiso(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'role_permissions'
        managed = False
        unique_together = ('role_id', 'permission_id')

# ========================
# Tabla user_sessions
# ========================
class UserSession(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    token = models.CharField(max_length=500)
    ip_address = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_sessions'
        managed = False

    def __str__(self):
        return f"Session {self.id} - User {self.user_id}"


# ========================
# Tabla auth_logs
# ========================
class AuthLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    action = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'auth_logs'
        managed = False

    def __str__(self):
        return f"{self.action} - {self.status}"
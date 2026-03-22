from pydantic import BaseModel

# USERS
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# ROLES
class RoleCreate(BaseModel):
    name: str
    description: str

# PERMISSIONS
class PermissionCreate(BaseModel):
    name: str
    description: str

# ROLE-PERMISSION
class RolePermissionCreate(BaseModel):
    role_id: int
    permission_id: int

# USER SESSIONS
class UserSessionCreate(BaseModel):
    user_id: int
    token: str
    ip_address: str = None
    user_agent: str = None
    expires_at: str = None

# AUTH LOGS
class AuthLogCreate(BaseModel):
    user_id: int
    action: str
    ip_address: str = None
    user_agent: str = None
    status: str
from rest_framework import permissions
from .models import User

class IsAdminUserRole(permissions.BasePermission):
    def has_permission(self, request, view): # added user authentication
        if not request.user.is_authenticated:
            return False
        
        try:
            user = User.objects.get(email=request.user.email)
        except User.DoesNotExist:
            return False

        return user.role == "admin"

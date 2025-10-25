import logging
from rest_framework import permissions
from .models import User

logger = logging.getLogger(__name__)


class IsAdminUserRole(permissions.BasePermission):
    def has_permission(self, request, view): # added user authentication
        if not request.user.is_authenticated:
            logger.error("Error: User not authenticated.")
            return False
        
        try:
            user = User.objects.get(email=request.user.email)
        except User.DoesNotExist:
            logger.error(f"Error: User not found ({request.user.email})")
            return False

        if user.role != "admin":
            logger.error(f"Error: User is not an admin ({request.user.email})")
            return False

        return True

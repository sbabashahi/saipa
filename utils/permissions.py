from rest_framework import permissions


class SuperUserPermission(permissions.BasePermission):
    """
    Global permission Super user
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

from rest_framework import permissions


class IsSuperadmin(permissions.BasePermission):
    """
        Custom permission to only allow superadmins.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "superadmin")


class IsManager(permissions.BasePermission):
    """
        Custom permission to only allow Managers.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "manager")


class IsSuperadminOrManager(permissions.BasePermission):
    """
        Custom permission to allow superadmins and managers.
    """
    def has_permission(self, request, view):
        is_true = (
            request.user.role == "superadmin" or
            request.user.role == "manager"
        )
        return bool(request.user and is_true)

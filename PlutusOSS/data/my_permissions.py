from rest_framework import permissions


class IsAdminOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission: admin can edit, authenticated user only read (safe_methods)
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_staff

        return False

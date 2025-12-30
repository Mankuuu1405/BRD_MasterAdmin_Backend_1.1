from rest_framework.permissions import BasePermission


class IsHomeDashboardAllowed(BasePermission):
    """
    RBAC for Home Dashboard
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        role = getattr(request.user, "role", None)

        if role in ["SUPER_ADMIN", "MASTER_ADMIN"]:
            return True

        if role == "ORG_ADMIN" and request.method == "GET":
            return True

        return False

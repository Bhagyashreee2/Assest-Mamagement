from rest_framework.permissions import BasePermission

class IsAdminOrTokenAuthenticated(BasePermission):
    """
    Allows access to admin users or if the user is authenticated with a token.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Allow access for authenticated users
            return True
        elif request.user.is_staff and request.method == 'POST':
            # Allow access for admin users making POST requests
            return True
        else:
            # Deny access for other users
            return False
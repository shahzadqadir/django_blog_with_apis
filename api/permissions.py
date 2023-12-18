from rest_framework import permissions


class PostPermissions(permissions.BasePermission):
    message = f"Access Denied"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True
        else:
            self.message = f"Access denied to {request.user} as this post belongs to {obj.author}"
            return False
        
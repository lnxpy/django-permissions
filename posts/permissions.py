from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-Only Permissions are Allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write Permissions are Allowed to the author of the post
        return obj.author == request.user

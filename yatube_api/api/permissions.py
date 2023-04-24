from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    message = 'Вы не можете выполнять операции с чужим контентом.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)

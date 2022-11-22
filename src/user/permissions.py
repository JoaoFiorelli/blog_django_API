from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permite o usuário atualizar apenas seu perfil"""

    def has_object_permission(self, request, view, obj):
        """Checa se o usuário tem permissão para edição"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

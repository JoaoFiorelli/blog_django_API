from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class UserViewSet(viewsets.ModelViewSet):
    """Usuário ViewSet"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """Cria o token de autenticação"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

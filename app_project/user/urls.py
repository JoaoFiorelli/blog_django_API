from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginApiView


router = DefaultRouter()
router.register('user-profile', UserViewSet)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

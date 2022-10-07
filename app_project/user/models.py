from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager de UserProfile"""

    def create_user(self, name, email, password=None):
        """Cria um novo perfil de usuário"""

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        """Cria um novo super usuário"""

        user = self.create_user(name, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model para armazenar dados básicos dos usuários"""

    name = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

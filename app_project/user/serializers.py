from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer"""

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Cria um usuário"""

        user = UserProfile.objects.create(
            name=validated_data['name'], 
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

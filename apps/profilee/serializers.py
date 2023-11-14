from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ProfileUser
from django.core.exceptions import ValidationError

User = get_user_model()


class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


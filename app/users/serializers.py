from adrf.serializers import ModelSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.fields import IntegerField

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ListUsersSerializer(ModelSerializer):
    users = SimpleUserSerializer(many=True)
    class Meta:
        model = User
        fields = ['users']

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }
        
    async def acreate(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return await super().acreate(validated_data)
    

class DeleteUserSerializer(ModelSerializer):
    id = IntegerField(help_text="ID użytkownika")
    class Meta:
        model = User
        fields = ['id']



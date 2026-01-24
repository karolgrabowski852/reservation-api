from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ListUsersSerializer(serializers.Serializer):
    users = SimpleUserSerializer(many=True)
    class Meta:
        fields = ['users']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return super().create(validated_data)
    

class DeleteUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text="ID użytkownika")
    class Meta:
        fields = ['id']



from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=5)
    email = serializers.EmailField(max_length=255, min_length=8),
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate(self, attrs): 
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username':('Username is already exist')})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':('Email is already exist')})
    
        return super().validate(attrs)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):

    class Meta: 
        model = User
        fields = ['username', 'password']
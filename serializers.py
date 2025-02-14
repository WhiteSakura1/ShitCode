from rest_framework import serializers
from .models import  User
from django.contrib.auth import authenticate
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
    def save(self, *args , **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password , password2 = self.validated_data['password'] , self.validated_data['password2']
        if password2 != password:
            raise serializers.ValidationError(
                {
                    'msg':'Пароли не совпадают'
                }
            )
        user.set_password(password)
        user.save()
        self.user = user

        return user

class UserLoginSerializer(serializers.Serializer):
    user:User = None
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user:
            return  user

        return False

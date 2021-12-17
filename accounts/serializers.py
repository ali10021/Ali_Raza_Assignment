from rest_framework import serializers
from .models import(
    User,
    Country,
)
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    
    confirmPassword = serializers.CharField(max_length=200, write_only=True)
    
    class Meta:
        model = User
        fields = ('email','password', 'confirmPassword', 'name', 'gender', 'age', 'city',)
        write_only_fields = ['confirmPassword']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
        
    def validate(self, attrs):
        if self.instance != None:
            if attrs.get('confirmPassword'):        
                if attrs['confirmPassword'] == attrs['password']:
                    del attrs['confirmPassword']
                    return super().validate(attrs)
                else:
                    raise serializers.ValidationError("passwords did not match")
            else:
                return super().validate(attrs)
        
        else:
            if attrs['confirmPassword'] == attrs['password']:
                del attrs['confirmPassword']
                return super().validate(attrs)
            else:
                raise serializers.ValidationError("passwords did not match")    
        
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        # hashing the password for security
        user.set_password(user.password)
        user.is_staff = True
        user.save()
        return user
    
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
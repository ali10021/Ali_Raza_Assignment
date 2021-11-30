from rest_framework import serializers
from .models import(
    User,
    Country,
    SalesData,
)
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    
    # adding an extra field to serializers to validate password
    confirmPassword = serializers.CharField(max_length=200, write_only=True)
    
    class Meta:
        model = User
        fields = ('email','password', 'confirmPassword', 'name', 'gender', 'age', 'city',)
    
    # Overwriting the create method for password validation check
    def create(self, validated_data):
        print("i am in create emthod of serializer")
        country = Country.objects.create(name="Russia")
        if validated_data['confirmPassword'] == validated_data['password']:
            # deleting the 'confirmPassword' key from dict 'validated_data' so user can be created
            del validated_data['confirmPassword']
            user = User.objects.create(**validated_data)
            # hashing the password for security
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            return user
        else:
            raise serializers.ValidationError({'Password': 'Passwords did not match'})
    
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    
    
class SalesDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalesData
        fields = ('date', 'product', 'sales_number', 'revenue', 'user')
        

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('name', 'city')
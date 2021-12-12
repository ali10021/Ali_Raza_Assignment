from django.http import request
from rest_framework import serializers
from accounts.serializers import UserSerializer
from sales.models import(
    SalesData,
    Country
)
from django.db import models


class SalesDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalesData
        fields = ('id' ,'date', 'product', 'sales_number', 'revenue', 'user')
        
    def create(self, validated_data):
        print(self.context['request'].user)
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('id' ,'name', 'city')